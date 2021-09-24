import unittest
from typing import List

from classes.terra import Terra


class TestTerra(unittest.TestCase):

    def test_generate_wallet_01(self):
        mnemonics: List[str] = ['charge', 'rotate', 'december', 'sense', 'wood', 'struggle', 'cradle', 'retire', 'file',
                                'umbrella', 'render', 'route', 'hurry', 'miracle', 'maximum', 'unfair', 'people',
                                'twelve', 'hazard', 'fog', 'dog', 'guard', 'quote', 'nominee']
        wallet = Terra.generate_wallet(mnemonics)
        self.assertEqual(wallet, {
            'private_key': '9dbabe24fee2230090780a0661de70b0b453f33269ae3c5a22ae3884a4e43337',
            'public_key': '02b312a438a0ea3664b7564336162f2769d99e8589d984afead3c326e0709749bc',
            'terra_address': 'terra15pe2gfxly2qs3w42kfrfd278c23mu5cxah48he'
        })

    def test_generate_wallet_02(self):
        mnemonics: List[str] = ['much', 'six', 'destroy', 'pulse', 'melody', 'marble', 'monster', 'neglect', 'enough',
                                'gorilla', 'vacant', 'artwork', 'fade', 'remove', 'trumpet', 'inside', 'shoulder',
                                'any', 'cattle', 'hub', 'shrimp', 'mercy', 'lesson', 'undo']
        wallet = Terra.generate_wallet(mnemonics)
        self.assertEqual(wallet, {
            'private_key': '431517dce4592a198ec246d46cacb8e1c90545ed2172ac7eb79a5ffbc0126685',
            'public_key': '02d4e5a26331067f2092a95dd63b810a1a557a7a107ab0a97334ea088db51b913b',
            'terra_address': 'terra1v0sc4g7wzada4c0747myysnrludc6dur0jxn24'
        })
