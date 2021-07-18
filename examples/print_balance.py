import os
import traceback
from rich import print

from binaryapi.stable_api import Binary

token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

if __name__ == '__main__':
    binary = Binary(token=token)
    print('Logged in')

    balance = binary.api.profile.balance
    currency = binary.api.profile.currency

    print('Balance: {:.2f} {}'.format(balance, currency))
