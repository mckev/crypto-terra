"""
Generate Terra wallets which have predefined prefix.
"""
from typing import List

from classes.bip39 import Bip39
from classes.terra import Terra

while True:
    mnemonics: List[str] = Bip39.generate_random_mnemonics()
    wallet = Terra.generate_wallet(mnemonics)
    if wallet['terra_address'].startswith('terra1kev'):
        print(f'{mnemonics}: {wallet["terra_address"]}')
