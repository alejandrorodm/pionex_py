from pionex_python.internal.generate_signature import rest_signature
from pionex_python.internal.PionexExceptions import REST_Exception
from pionex_python import __version__

import requests
import time
import json

class RestClient:
    def __init__(self, key:str='', secret:str=''):
        self.base_url = 'https://api.pionex.com/'
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'pionex-python/{__version__}',
            'Content-Type': 'application/json;charset=utf-8',
        })
        if key:
            self.session.headers.update({
                'PIONEX-KEY':key
            })

    def _send_request(self, http_method, url_path, **params):
        url = self.base_url + url_path
        params = {k: v for k, v in params.items() if v is not None}  # Remove None params

        timestamp = str(int(time.time() * 1000))
        params['timestamp'] = timestamp

        if 'data' in params:
            data = params['data']
            del params['data']
        else:
            data = None

        if self.key:
            signature = rest_signature(self.secret, http_method, url_path, timestamp, params, data)
            self.session.headers.update({
                'PIONEX-KEY': self.key,
                'PIONEX-SIGNATURE': signature
            })

        match(http_method):
            case 'GET':
                r = self.session.get(url, params=params, json=data)
            case 'DELETE':
                r = self.session.delete(url, params=params, json=data)
            case 'PUT':
                r = self.session.put(url, params=params, json=data)
            case 'POST':
                r = self.session.post(url, params=params, json=data)
            case _:
                raise REST_Exception('Unsupported HTTP method')

        response = r.json()

        if not response['result']:
            raise REST_Exception(response)
        return response
