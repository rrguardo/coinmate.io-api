Coinmate.io API wrapper
-----------------------

Basic CoinMate.io API wrapper, that support get the balance, withdrawal
and more ::

    from coinmate_api import coinmate
    cm_api = coinmate('privateApiKey', 'publicApiKey', 'client_id')
    print cm_api.get_eur_available()
    result = cm_api.withdraw_bitcoins(0.01,'1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
    if not result['error']:
        print "Transaction ID:"
        print result['data']
    ticker_info = cm_api.get_ticker()
