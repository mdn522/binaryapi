# This code is untested. bug shall be fixed upon reporting
from rich.console import Console
from threading import Thread
from typing import Optional
from rich import print
import time
import os

from binaryapi.stable_api import Binary

# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)
binary: Optional[Binary] = None


# noinspection PyShadowingNames,PyBroadException
def check_connect_helper(api_client: Optional[Binary], on_connect=None, *args, **kwargs) -> Binary:
    retry_times = 0
    while not api_client or not api_client.check_connect():
        # noinspection PyBroadException
        try:
            api_client.api.connect()
            console.log('Reconnected!')

            if callable(on_connect):
                on_connect(api_client)
        except Exception:
            if retry_times < 3:
                retry_times = retry_times + 1
                console.log('Retry connect #' + str(retry_times))
            else:
                try:
                    del api_client
                except Exception:
                    pass

                api_client = None

                try:
                    api_client = Binary(*args, **kwargs)
                    retry_times = 0
                    console.log('Reconnected API')

                    if callable(on_connect):
                        on_connect(api_client)
                except Exception:
                    console.print_exception()

        time.sleep(1)  # seconds

    return api_client


def check_connect():
    global binary

    while True:
        binary = check_connect_helper(api_client=binary, on_connect=on_connect, token=token, message_callback=message_handler)
        time.sleep(1)  # seconds


# Execute this function whenever api connects/reconnects
# noinspection PyShadowingNames
def on_connect(binary: Binary):
    console.log('On Connect')
    pass


# Message callback/handler
def message_handler(message: dict):
    msg_type = message.get('msg_type')

    print(msg_type, "=>", message)


if __name__ == "__main__":
    binary = Binary(token=token, message_callback=message_handler)
    print('Logged in')
    
    on_connect(binary)

    check_connect_thread = Thread(target=check_connect, args=(), daemon=True)
    check_connect_thread.start()

    while True:
        try:
            # balance = binary.api.profile.balance
            # currency = binary.api.profile.currency
            # print('Balance: {:.2f} {}'.format(balance, currency))

            time.sleep(1)  # seconds
        except KeyboardInterrupt:
            break
