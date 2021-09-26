import unittest
from typing import List

from classes.util import Util


class TestUtil(unittest.TestCase):

    def test_base32encode(self):
        # Ref: https://en.bitcoin.it/wiki/Bech32
        data: bytes = bytes.fromhex('751e76e8199196d454941c45d1b3a323f1433bd6')
        data_in_base32: List[int] = Util.split_bits(data, 5)
        expected: List[int] = [14, 20, 15, 7, 13, 26, 0, 25, 18, 6, 11, 13, 8, 21, 4, 20, 3, 17, 2, 29, 3, 12, 29, 3, 4,
                               15, 24, 20, 6, 14, 30, 22]
        self.assertEqual(data_in_base32, expected)

    def test_base8encode(self):
        data: bytes = bytes.fromhex('08')
        data_in_base32: List[int] = Util.split_bits(data, 5)
        self.assertEqual(data_in_base32, [0, 8])
