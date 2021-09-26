from typing import List, Optional

from classes.util import Util


class Bech32:
    CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'

    @staticmethod
    def bech32_polymod(data_in_base32: List[int]) -> int:
        # Compute the Bech32 checksum
        # Ref: https://github.com/fiatjaf/bech32/blob/master/bech32/__init__.py
        generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
        chk: int = 1
        for value in data_in_base32:
            top = chk >> 25
            chk = (chk & 0x1ffffff) << 5 ^ value
            for i in range(5):
                chk ^= generator[i] if ((top >> i) & 1) else 0
        return chk

    @staticmethod
    def bech32_hrp_expand(hrp: str) -> List[int]:
        # The last 3 bits of hrp, followed by 0, then the first 5 bits of hrp
        # For example: 'bc' = 01100010 01100011
        #              becomes [011, 011, 0, 00010, 00011] or [3, 3, 0, 2, 3]
        return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]

    @staticmethod
    def bech32_create_checksum(hrp: str, data_in_base32: List[int]) -> List[int]:
        hrp_expand: List[int] = Bech32.bech32_hrp_expand(hrp)
        polymod: int = Bech32.bech32_polymod(hrp_expand + data_in_base32 + [0, 0, 0, 0, 0, 0]) ^ 1
        return [(polymod >> 5 * (5 - i)) & 31 for i in range(6)]

    @staticmethod
    def bech32_encode(hrp: str, witver: Optional[int], data: bytes) -> str:
        data_in_base32: List[int] = Util.split_bits(data, 5)
        if witver is not None:
            data_in_base32 = [witver] + data_in_base32
        data_in_base32 += Bech32.bech32_create_checksum(hrp, data_in_base32)
        return hrp + '1' + ''.join([Bech32.CHARSET[d] for d in data_in_base32])
