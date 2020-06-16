# Binary.com API for Python

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/mdn522)


## About API

```python
# High Level API, This API is based on "binaryapi.api" for easy usage
from binaryapi.stable_api import Binary
# Low Level API
from binaryapi.api import BinaryAPI
```

## Installing and Updating
For Python 3
```bash
pip3 install -U git+git://github.com/mdn522/binaryapi.git
```

---
## Getting Started
```python
import time
from binaryapi.stable_api import BinaryAPI

binary_token = "YOUR-API-TOKEN-GOES-HERE"

binary = IQ_Option(token=binary_token)

symbol = "frxEURUSD"
print("Buy a CALL contract")
print(binary.buy_call_put('CALL', amount=1, symbol=symbol, duration=5, duration_unit='t'))
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
### Login

```python
binary = Binary(token="YOUR-API-TOKEN-GOES-HERE")
```

---