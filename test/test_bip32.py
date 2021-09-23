import unittest

from classes.bip32 import Bip32


class TestBip32(unittest.TestCase):

    def test_from_seed_01(self):
        seed: bytes = bytes.fromhex(
            'bda85446c68413707090a52022edd26a1c9462295029f2e60cd7c4f2bbd3097170af7a4d73245cafa9c3cca8d561a7c3de6f5d4a10be8ed2a5e608d68f92fcc8')
        chain_code, private_key = Bip32.from_seed(seed)
        self.assertEqual(list(chain_code),
                         [97, 204, 178, 187, 231, 210, 164, 252, 205, 95, 65, 142, 233, 49, 219, 124, 186, 201, 161, 83,
                          236, 67, 176, 174, 55, 89, 255, 153, 30, 77, 35, 209])
        self.assertEqual(list(private_key),
                         [200, 180, 7, 60, 207, 204, 99, 71, 92, 61, 82, 2, 198, 89, 68, 132, 238, 78, 119, 184, 103,
                          205, 227, 195, 180, 100, 50, 253, 113, 180, 103, 174])

    def test_from_seed_02(self):
        seed: bytes = bytes.fromhex(
            '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
        chain_code, private_key = Bip32.from_seed(seed)
        self.assertEqual(list(chain_code),
                         [109, 248, 59, 18, 64, 116, 25, 19, 152, 132, 189, 70, 73, 126, 159, 250, 191, 41, 255, 153,
                          124, 132, 176, 14, 91, 81, 140, 208, 97, 8, 164, 39])
        self.assertEqual(list(private_key),
                         [103, 155, 249, 44, 4, 207, 22, 48, 112, 83, 203, 237, 51, 120, 79, 60, 66, 102, 179, 98, 191,
                          95, 61, 126, 225, 59, 237, 111, 39, 25, 116, 60])

    def test_derive_keypair(self):
        seed: bytes = bytes.fromhex(
            '01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998')
        chain_code, private_key = Bip32.from_seed(seed)
        private_key, public_key = Bip32.derive_keypair(chain_code, private_key)
        self.assertEqual(list(private_key),
                         [241, 30, 159, 70, 151, 85, 13, 83, 196, 100, 43, 107, 132, 25, 191, 13, 254, 112, 52, 69, 181,
                          248, 165, 73, 200, 54, 211, 246, 54, 21, 211, 155])
        self.assertEqual(list(public_key),
                         [3, 122, 144, 226, 118, 130, 155, 221, 165, 54, 192, 189, 210, 143, 63, 31, 52, 108, 225, 168,
                          16, 105, 160, 134, 45, 65, 7, 36, 229, 93, 124, 232, 227])
