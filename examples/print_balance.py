import os
import traceback
try:
    from rich import print
except ImportError:
    pass

from binaryapi.stable_api import Binary

token = os.environ.get('BINARY_TOKEN', 'YOU BINARY TOKEN GOES HERE')
assert token != 'YOU BINARY TOKEN GOES HERE', "Please assign a token"


if __name__ == '__main__':
    binary = Binary(token=token)
    print('Logged in')

    balance = binary.api.profile.balance
    currency = binary.api.profile.currency

    print('Balance: {:.2f} {}'.format(balance, currency))
