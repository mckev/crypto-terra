import hashlib
from typing import List, Any

from classes.bech32 import Bech32
from classes.bip32 import Bip32
from classes.bip39 import Bip39


class Terra:

    @staticmethod
    def create_terra_address(public_key: bytes) -> str:
        # Ref: https://github.com/terra-money/station-electron/blob/main/public/wallet.js
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(hashlib.sha256(public_key).digest())
        public_key_hashed = ripemd160.digest()
        return Bech32.bech32_encode(hrp='terra', witver=None, data=public_key_hashed)

    @staticmethod
    def generate_wallet(mnemonics: List[str]) -> Any:
        # Ref: https://github.com/terra-money/station-electron/blob/main/public/wallet.js
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics)
        chain_code, private_key = Bip32.from_seed(seed)
        private_key, public_key = Bip32.derive_keypair(chain_code, private_key)
        terra_address: str = Terra.create_terra_address(public_key)
        return {
            'private_key': private_key.hex(),
            'public_key': public_key.hex(),
            'terra_address': terra_address
        }
