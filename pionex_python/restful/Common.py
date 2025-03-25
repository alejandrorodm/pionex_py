from pionex_python.internal.RestClient import RestClient
from pionex_python.internal.PionexExceptions import assert_valid_market_type

#rename python function so we can have "type" argument
type_func = type

class Common(RestClient):
    def __init__(self):
        super().__init__()

    def market_data(self, symbols:list[str]=None, market_type='PERP'):
        """
        Fetches market data for all symbols or a specific symbol.
        
        Parameters:
            symbols (list[str], optional): List of symbols. (Optional)
            type (str, optional): PERP, SPOT. (Optional)
        Returns:
            Response object from the API request.
        """
        assert_valid_market_type(market_type)
        if type_func(symbols) == list:
            symbols = ','.join(symbols)
        return self._send_request('GET', '/api/v1/common/symbols', symbols=symbols, type=market_type)

    def klines(self, symbol:str, interval:str, endTime:int=None, limit:int=None):
        """
        Fetches kline (candlestick) data for a given symbol and interval.
        
        Parameters:
            symbol (str): Symbol. (Mandatory)
            interval (str): 1M, 5M, 15M, 30M, 60M, 4H, 8H, 12H, 1D. (Mandatory)
            endTime (int, optional): End time in milliseconds. (Optional)
            limit (int, optional): Default 100, range: 1-500. (Optional)
        Returns:
            Response object from the API request.
            
        Example: https://api.pionex.com/api/v1/market/klines?symbol=BTC_USDT&interval=5M
        """
        return self._send_request('GET', '/api/v1/market/klines', symbol=symbol, interval=interval, endTime=endTime, limit=limit)