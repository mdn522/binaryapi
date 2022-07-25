# Binary.com & Deriv.com API for Python

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/mdn522)


## About API

```python
# High Level API, This API is based on "binaryapi.api" for easy usage
from binaryapi.stable_api import Binary

# Low Level API
from binaryapi.api import BinaryAPI
```

## Compatibility

Requires **Python 3.7.0** or later.

## Installing and Updating
```bash
pip install -U git+https://github.com/mdn522/binaryapi.git
```
Must have git installed

---
## Getting Started
```python
from binaryapi.stable_api import Binary

binary_token = "YOUR-API-TOKEN-GOES-HERE"

binary = Binary(token=binary_token)

symbol = "frxEURUSD"  # symbol/asset

print("Buy a [CALL] contract")
success, contract_id, req_id = binary.buy('CALL', amount=1, symbol=symbol, duration=5, duration_unit='t')

print('success={}, contract_id={}, req_id={}'.format(success, contract_id, req_id))
```

---

## Document

### Import 
```python
from binaryapi.stable_api import Binary
```
---
### Enabling Debug Logs

```python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
```
---
### Authorize/Login

```python
binary = Binary(token="YOUR-API-TOKEN-GOES-HERE")
```

*It automatically subscribes to `balance` and `transaction` API

### Authorize/Login with a message handler function
```python
def message_handler(message):
    msg_type = message.get('msg_type')
    
    print(msg_type, "=>", message)

    
binary = Binary(token="YOUR-API-TOKEN-GOES-HERE", message_callback=message_handler)
```



---
I tried to add every API function available in Binary.com API documentation to this library, which you can call by accessing `api` variable of stable API

Examples:
```python
binary = Binary(token="YOUR-API-TOKEN-GOES-HERE")

# Buy API - https://developers.binary.com/api/#buy
binary.api.buy(buy, price, parameters=None, subscribe=None, passthrough=None, req_id=None)
# You must pass values for "buy" and "price" arguments

# Proposal API - https://developers.binary.com/api/#proposal
binary.api.proposal(contract_type, currency, symbol, amount=None, barrier=None, barrier2=None, basis=None, cancellation=None, date_expiry=None, date_start=None, duration=None, duration_unit=None, limit_order=None, multiplier=None, product_type=None, selected_tick=None, subscribe=None, trading_period_start=None, passthrough=None, req_id=None)
# You must pass values for "contract_type", "currency" and "symbol" arguments

# Subscribe to Ticks API - https://developers.binary.com/api/#ticks
binary.api.ticks(ticks="frxEURUSD", subscribe=None, passthrough=None, req_id=None)

# For More API functions/endpoints please refer to https://developers.binary.com/api/
```