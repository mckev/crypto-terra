import unittest
from typing import List

from classes.bip39 import Bip39


class TestBip39(unittest.TestCase):

    def test_mnemonics_to_seed_01(self):
        mnemonics: List[str] = ['charge', 'rotate', 'december', 'sense', 'wood', 'struggle', 'cradle', 'retire', 'file',
                                'umbrella', 'render', 'route', 'hurry', 'miracle', 'maximum', 'unfair', 'people',
                                'twelve', 'hazard', 'fog', 'dog', 'guard', 'quote', 'nominee']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics)
        self.assertEqual(list(seed),
                         [143, 13, 172, 146, 213, 216, 81, 162, 144, 45, 79, 148, 253, 133, 189, 84, 45, 193, 171, 121,
                          132, 69, 87, 243, 203, 213, 179, 126, 222, 150, 241, 213, 241, 6, 217, 175, 99, 195, 13, 159,
                          31, 56, 96, 15, 9, 207, 218, 144, 138, 246, 201, 192, 61, 65, 233, 220, 201, 231, 178, 52,
                          197, 234, 186, 85])

    def test_mnemonics_to_seed_02(self):
        mnemonics: List[str] = ['much', 'six', 'destroy', 'pulse', 'melody', 'marble', 'monster', 'neglect', 'enough',
                                'gorilla', 'vacant', 'artwork', 'fade', 'remove', 'trumpet', 'inside', 'shoulder',
                                'any', 'cattle', 'hub', 'shrimp', 'mercy', 'lesson', 'undo']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics)
        self.assertEqual(list(seed),
                         [84, 244, 138, 129, 59, 53, 173, 29, 71, 51, 148, 172, 101, 154, 209, 153, 65, 150, 2, 7, 2,
                          252, 227, 98, 197, 88, 98, 193, 60, 254, 92, 189, 228, 226, 220, 76, 69, 248, 224, 110, 34,
                          75, 116, 187, 20, 253, 204, 166, 43, 41, 209, 116, 194, 188, 237, 87, 233, 117, 44, 186, 143,
                          190, 33, 1])
