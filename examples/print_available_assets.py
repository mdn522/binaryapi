# Print list of available assets
# https://developers.binary.com/api/#asset_index
import os
import time
from rich.console import Console
from binaryapi.stable_api import Binary

# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)


if __name__ == '__main__':
    binary = Binary(token=token)
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
