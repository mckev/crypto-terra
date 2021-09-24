from typing import List


class Util:

    @staticmethod
    def split_bits(b: bytes, n: int) -> List[int]:
        """ Split bytes into a list of n-bit integers """
        # Convert to binary
        binary: str = ''
        for i in b:
            binary += bin(i).lstrip('0b').zfill(8)
        # Split
        parts = [binary[i:i + n] for i in range(0, len(binary), n)]
        # Convert to integers
        parts = [int(part, 2) for part in parts]
        return parts
