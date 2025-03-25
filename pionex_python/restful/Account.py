from pionex_python.internal.RestClient import RestClient

class Account(RestClient):
    def __init__(self, key, secret):
        super().__init__(key, secret)

    def get_balance(self, coin=None):
        if coin is None:
            return self._send_request('GET', '/api/v1/account/balances')
        else:
            result = self._send_request('GET', '/api/v1/account/balances')
            return next(
                (balance['free'] for balance in result['data']['balances'] if balance['coin'] == coin), 
                0
            )
        