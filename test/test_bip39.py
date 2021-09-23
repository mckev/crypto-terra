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

    def test_mnemonics_to_seed_03(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: List[str] = ['abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon',
                                'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon',
                                'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'abandon', 'art']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         'bda85446c68413707090a52022edd26a1c9462295029f2e60cd7c4f2bbd3097170af7a4d73245cafa9c3cca8d561a7c3de6f5d4a10be8ed2a5e608d68f92fcc8')

    def test_mnemonics_to_seed_04(self):
        # Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#Test_vectors
        mnemonics: List[str] = ['void', 'come', 'effort', 'suffer', 'camp', 'survey', 'warrior', 'heavy', 'shoot',
                                'primary', 'clutch', 'crush', 'open', 'amazing', 'screen', 'patrol', 'group', 'space',
                                'point', 'ten', 'exist', 'slush', 'involve', 'unfold']
        seed: bytes = Bip39.mnemonics_to_seed(mnemonics, passphrase='TREZOR')
        self.assertEqual(seed.hex(),
                         '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
