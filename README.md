# 🚀 Pionex to Python

Easily interact with the [Pionex API](https://pionex-doc.gitbook.io/apidocs) for both REST and WebSocket connections.

## 📦 Installation
```sh
pip install pionex_py
```

## 📝 Description
Pionex to Python is a connector library for Pionex's REST and WebSocket API.
- Mirrors the official [Pionex API documentation](https://pionex-doc.gitbook.io/apidocs) for intuitive implementation.
- Supports both public and private API endpoints.
- Clean, modular, and easy-to-extend codebase.

Check out the [GitHub project](https://github.com/alejandrorodm/pionex_py) for more details.

## ⚡ Features
- ✅ **Full REST API support** (public and private endpoints)
- ✅ **Real-time WebSocket streaming**
- ✅ **Handles multiple orders with ease**
- ✅ **Error handling**
- ✅ **Lightweight and fast**

## 🚀 Quickstart

### 📌 REST API Examples

#### Public Endpoint
```python
from pionex_py.restful.Common import Common

commonClient = Common()
market_data = commonClient.market_data()

print(market_data)
```

#### Private Endpoint
```python
from pionex_py.restful.Orders import Orders

key, secret = 'X...X', 'X...X'

ordersClient = Orders(key, secret)

order = {
    'symbol': 'BTC_USDT',
    'side': 'BUY',
    'type': 'MARKET',
    'amount': '16',
}

response = ordersClient.new_order(order=order)
print(response)
```

<details>
  <summary>📌 Multiple Order Template</summary>

  ```python
  from pionex_py.restful.Orders import Orders

  key, secret = 'X...X', 'X...X'

  ordersClient = Orders(key, secret)

  orders = [
    {
      'side': 'BUY',
      'type': 'LIMIT',
      'price': '57200',
      'size': '0.0002'
    },
    {
      'side': 'SELL',
      'type': 'LIMIT',
      'price': '60000',
      'size': '0.0002'
    }
  ]

  response = ordersClient.new_multiple_order(symbol='BTC_USDT', orders=orders)
  print(response)
  ```
</details>

### 📡 WebSocket Example
```python
from pionex_py.websocket.PublicStream import PublicStream
from time import sleep

# For private streams: stream = PrivateStream(key, secret)
stream = PublicStream()

def onMessage(msg):
    print(msg)

stream.subscribe(callback=onMessage, topic='TRADE', symbol='BTC_USDT')
stream.subscribe(callback=onMessage, topic='TRADE', symbol='ETH_USDT')

sleep(5)

stream.unsubscribe(topic='TRADE', symbol='BTC_USDT')
stream.unsubscribe(topic='TRADE', symbol='ETH_USDT')
```

## 🔧 TODOs & Future Enhancements
- [ ] Reconnection handling for WebSockets
- [ ] Improved error handling with retries
- [ ] More endpoint coverage
- [ ] CLI for quick trading actions

## 📬 Contributions
Pull requests are welcome! If you find a bug or want to propose an enhancement, feel free to [open an issue](https://github.com/alejandrorodm/pionex_py/issues).

## 🛠️ License
This project is licensed under the MIT License - see the LICENSE file for details.

