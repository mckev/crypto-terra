import hashlib
import hmac
from typing import List

import coincurve  # pip install coincurve


class Bip32:
    """ Hierarchical Deterministic Wallets """

    HARDENED_INDEX = 0x80000000

    @staticmethod
    def from_seed(seed: bytes):
        secret: bytes = hmac.new(key=b'Bitcoin seed', msg=seed, digestmod=hashlib.sha512).digest()
        chain_code: bytes = secret[32:]
        private_key: bytes = secret[:32]
        return chain_code, private_key

    @staticmethod
    def derive_keypair(chain_code: bytes, private_key: bytes, bip: int = None):
        if bip is None:
            path: str = "m/44'/330'/0'/0/0"
        else:
            path: str = f"m/44'/{bip}'/0'/0/0"
        paths: List[int] = []
        for index in path.split('/')[1:]:
            if index[-1] in ["'", 'h', 'H']:
                paths.append(int(index[:-1]) + Bip32.HARDENED_INDEX)
            else:
                paths.append(int(index))

        for index in paths:
            if index & Bip32.HARDENED_INDEX:
                payload: bytes = hmac.new(key=chain_code, msg=b'\x00' + private_key + index.to_bytes(4, 'big'),
                                          digestmod=hashlib.sha512).digest()
                child_private = coincurve.PrivateKey(payload[:32]).add(private_key)
                chain_code, private_key = payload[32:], child_private.secret
            else:
                public_key: bytes = coincurve.PublicKey.from_secret(private_key).format()
                payload: bytes = hmac.new(key=chain_code, msg=public_key + index.to_bytes(4, 'big'),
                                          digestmod=hashlib.sha512).digest()
                child_private = coincurve.PrivateKey(payload[:32]).add(private_key)
                chain_code, private_key = payload[32:], child_private.secret

        public_key: bytes = coincurve.PublicKey.from_secret(private_key).format()
        return private_key, public_key
