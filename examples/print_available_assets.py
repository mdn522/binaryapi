# Print list of available assets
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

    # Send asset index request
    asset_index_req_id = binary.api.asset_index()
    # Wait for asset index response
    binary.api.wait_for_response_by_req_id(req_id=asset_index_req_id)
    # Get asset index response
    asset_index_msg = binary.api.msg_by_req_id[asset_index_req_id]

    for asset in asset_index_msg['asset_index']:
        asset_name = asset[1]
        asset_code = asset[0]
        print('{}: {}'.format(asset_code, asset_name))
