# Prints balance when ever balance update received from server for 60 seconds
import os
import time
from rich.console import Console
from binaryapi.stable_api import Binary


# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)


def message_handler(message):
    msg_type = message.get('msg_type')

    if msg_type == 'balance':
        try:
            balance = message["balance"]["balance"]
            currency = binary.api.profile.currency

            console.log('Balance: {} {}'.format(balance, currency))
        except KeyError:
            console.print_exception()


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    console.log('Logged in')

    # Wait for 60 seconds then quit
    time.sleep(60)
