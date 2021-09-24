import unittest
from typing import List

from classes.bech32 import Bech32


class TestBech32(unittest.TestCase):

    def test_base32encode(self):
        # Ref: https://en.bitcoin.it/wiki/Bech32
        data: bytes = bytes.fromhex('751e76e8199196d454941c45d1b3a323f1433bd6')
        data_in_base32: List[int] = Bech32.base32encode(data)
        expected: List[int] = [14, 20, 15, 7, 13, 26, 0, 25, 18, 6, 11, 13, 8, 21, 4, 20, 3, 17, 2, 29, 3, 12,
                               29, 3, 4, 15, 24, 20, 6, 14, 30, 22]
        self.assertEqual(data_in_base32, expected)

    def test_bech32_create_checksum(self):
        data: bytes = bytes.fromhex('751e76e8199196d454941c45d1b3a323f1433bd6')
        data_in_base32: List[int] = Bech32.base32encode(data)
        witver: int = 0
        data_in_base32 = [witver] + data_in_base32
        chksum: List[int] = Bech32.bech32_create_checksum('bc', data_in_base32)
        expected: List[int] = [0x0c, 0x07, 0x09, 0x11, 0x0b, 0x15]
        self.assertEqual(chksum, expected)

    def test_bech32_encode(self):
        data: bytes = bytes.fromhex('751e76e8199196d454941c45d1b3a323f1433bd6')
        data_in_bech32: str = Bech32.bech32_encode(hrp='bc', witver=0, data=data)
        self.assertEqual(data_in_bech32, 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4')
