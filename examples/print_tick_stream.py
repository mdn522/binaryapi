# Prints ticks data for 60 seconds
import os
import time
from rich.console import Console
from binaryapi.stable_api import Binary

# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)


def message_handler(message):
    msg_type = message.get('msg_type')

    if msg_type == 'tick':
        # Print tick data from message
        console.print(message['tick'])


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    console.log('Logged in')

    # Symbol *can be an array of symbols too. eg: ['R_75', 'R_100'] etc.
    symbol = 'R_100'

    # Subscribe to ticks stream
    binary.api.ticks(symbol, subscribe=True)

    # Wait for 60 seconds then exit the script
    time.sleep(60)
