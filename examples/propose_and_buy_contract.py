# Proposes for a contract then buys it
import os
import time
from rich import print
from rich.console import Console

from binaryapi.constants import CONTRACT_TYPE, DURATION, PROPOSAL_BASIS
from binaryapi.exceptions import MessageByReqIDNotFound
from binaryapi.stable_api import Binary

# Binary Token
token = os.environ.get('BINARY_TOKEN', '<YOUR BINARY TOKEN GOES HERE>')

console = Console(log_path=False)


def message_handler(message):
    msg_type = message.get('msg_type')


# noinspection PyShadowingNames
def propose_and_buy(binary: Binary):
    account_currency = binary.api.profile.currency

    basis = PROPOSAL_BASIS.STAKE
    amount = 5
    symbol = 'R_75'
    duration = 5
    duration_unit = DURATION.TICK
    min_payout_pct = 0  # Minimum Payout %

    price = amount  # Maximum price at which to purchase the contract. used in buy() api

    # Yoo can add any parameter mentioned in the Binary developer api documentation
    # Binary API Documentation: https://developers.binary.com/api/#proposal
    # Deriv API Documentation: https://api.deriv.com/playground/#proposal
    proposal_req_id = binary.api.proposal(contract_type=CONTRACT_TYPE.CALL,
                                          basis=basis, amount=amount, currency=account_currency,
                                          symbol=symbol,
                                          duration=duration, duration_unit=duration_unit)

    # You can also subscribe to the proposal and wait for right opportunity and buy it
    # using the message_callback function.
    # but in this example it will instantly buy the contract if it's payout is greater than min_payout_pct or else exit the function
    try:
        # Wait for the response message for the proposal request
        binary.api.wait_for_response_by_req_id(req_id=proposal_req_id, type_name='proposal', max_timeout=5)
    except MessageByReqIDNotFound:
        console.log('[red]No proposal response from Binary websocket server')
        return

    # You can access to any message received by websocket server using req_id
    proposal_msg = binary.api.msg_by_req_id[proposal_req_id]

    if 'error' in proposal_msg:
        console.log('[red]Proposal error', proposal_msg['error'])
        return

    # We will use this buy_id to request the websocket server for buying the contract
    buy_id = None

    proposal_obj = proposal_msg['proposal']
    payout = (proposal_obj['payout'] - proposal_obj['ask_price']) / proposal_obj['ask_price'] * 100
    if payout >= min_payout_pct:
        buy_id = proposal_obj['id']
    else:
        console.log("[red]Payout lower than {}%".format(min_payout_pct))
        return

    # Request buy contract with buy_id
    # Binary API Documentation: https://developers.binary.com/api/#buy
    # Deriv API Documentation: https://api.deriv.com/playground/#buy
    buy_req_id = binary.api.buy(buy=buy_id, price=price)

    try:
        # Wait for the response message for the buy request
        binary.api.wait_for_response_by_req_id(req_id=buy_req_id, type_='buy')
    except MessageByReqIDNotFound:
        console.log("[red]No buy response from Binary websocket server")
        return

    buy_msg = binary.api.msg_by_type['buy'][buy_req_id]
    if 'error' in buy_msg:
        console.log('[red]Buy error', buy_msg['error'])
        return

    contract_id = buy_msg['buy']['contract_id']

    console.log("[green]Bought contract with contract_id: {}".format(contract_id))


if __name__ == '__main__':
    binary = Binary(token=token, message_callback=message_handler)
    console.log('Logged in')

    propose_and_buy(binary=binary)

    time.sleep(5)
