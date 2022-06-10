# Prints ticks_history data
# https://developers.binary.com/api/#ticks_history
import os
import time

from rich.console import Console
from binaryapi.stable_api import Binary

# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)


def message_handler(message):
    msg_type = message.get('msg_type')

    if msg_type in ['tick', 'history']:
        # Print tick data from message
        history_data = message['history']
        console.print(history_data)
    if msg_type in ['candles', 'ohlc']:
        # Print candles data from message
        candles_data = message['candles']
        console.print(candles_data)


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    console.log('Logged in')

    symbol = 'R_100'
    style = 'ticks'  # 'ticks' or 'candles'
    end = 'latest'  # 'latest' or unix epoch
    count = 10  # default: 5000 if not provided

    # Subscribe to ticks stream
    binary.api.ticks_history(
        ticks_history=symbol,
        style=style,
        count=count,
        end=end,
    )

    # Wait for 60 seconds then exit the script
    time.sleep(5)
