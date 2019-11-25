# -*- coding: utf-8 -*-
"""
    CoinMate.io unittests.
"""

import unittest
from coinmate_api import coinmate


class TestCoinmate(unittest.TestCase):
    """CoinMate.io unittests."""
    MOCK_API = True

    def setUp(self):
        self.cm = coinmate(privateApiKey=b'pub-key',
                           publicApiKey=b'prv-key',
                           clientId=b'100')
        if self.MOCK_API:
            self.cm.API_URL = \
                'https://private-anon-2d940214ba-coinmate.apiary-mock.com/api/'
        else:
            self.cm.API_URL = 'https://coinmate.io/api/'

    def test_balance(self):
        balances = self.cm.get_balance()
        assert 'data' in balances
        assert 'EUR' in balances['data']
        assert 'BTC' in balances['data']
        assert 'error' in balances

    def test_eur_balance(self):
        balances = self.cm.get_eur_balance()
        assert balances['currency'] == "EUR"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_btc_balance(self):
        balances = self.cm.get_btc_balance()
        assert balances['currency'] == "BTC"
        assert 'balance' in balances
        assert 'reserved' in balances
        assert 'available' in balances

    def test_eur_available(self):
        self.assertIs(type(self.cm.get_eur_available()), float)

    def test_btc_available(self):
        self.assertIs(type(self.cm.get_btc_available()), float)

    def test_withdraw_bitcoins(self):
        rs = self.cm.withdraw_bitcoins(1, '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
        assert not rs['error']
        self.assertIs(type(rs['data']), list)

    def test_get_ticker(self):
        ticker = self.cm.get_ticker()
        assert 'error' in ticker
        assert 'data' in ticker
        assert 'amount' in ticker['data']

    def test_get_ticker_low(self):
        ticker = self.cm.get_ticker_low()
        self.assertIs(type(ticker), float)

    def test_get_ticker_high(self):
        ticker = self.cm.get_ticker_high()
        self.assertIs(type(ticker), float)

    def test_get_ticker_last(self):
        ticker = self.cm.get_ticker_low()
        self.assertIs(type(ticker), float)

if __name__ == '__main__':
    unittest.main()
