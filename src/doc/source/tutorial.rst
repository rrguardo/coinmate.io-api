
Tutorial
--------

Basic Usage:
============

Get account balances ::

	from coinmate_api import coinmate
	cm_api = coinmate('privateApiKey', 'publicApiKey', 'client_id')
	btc_balance = cm_api.get_btc_balance()
	print "BTC balance: %s" % btc_balance
	
	eur_balance = cm_api.get_eur_balance()
	print "EUR balance: %s" % eur_balance


Withdraw bitcoins ::

	from coinmate_api import coinmate
	cm_api = coinmate('privateApiKey', 'publicApiKey', 'client_id')
	tid = cm_api.withdraw_bitcoins(0.01, '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
	print "Transaction ID: %s" % tid


Market Info Features:
=====================

Get Market Ticker Info ::

	from coinmate_api import coinmate
	cm_api = coinmate('privateApiKey', 'publicApiKey', 'client_id')
	
	ticker_low = cm_api.get_ticker_low()
	print "Ticker Low: %s" % ticker_low

	ticker_high = cm_api.get_ticker_high()
	print "Ticker High: %s" % ticker_high

	ticker_last = cm_api.get_ticker_last()
	print "Ticker Last: %s" % ticker_last
