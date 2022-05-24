# Simple Buy Example. Test it properly before using it for your self
import os
import time
import logging
import traceback
from rich import print

from binaryapi.constants import CONTRACT_TYPE, DURATION
from binaryapi.stable_api import Binary

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')


def message_handler(message):
    msg_type = message.get('msg_type')

    try:
        if msg_type in ['buy', 'proposal']:
            print(message)
    except Exception as e:
        traceback.print_exc()

    # print("MSG", message)


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    print('Logged in')

    success, contract_id, req_id = binary.buy(
        contract_type=CONTRACT_TYPE.CALL,
        amount=1, symbol='R_75',
        duration=5,
        duration_unit=DURATION.TICK
    )
    print({'success': success, 'contract_id': contract_id, 'req_id': req_id})

    time.sleep(20)
