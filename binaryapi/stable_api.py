from binaryapi.api import BinaryAPI
import binaryapi.constants as OP_code
import time
import logging

from collections import defaultdict


# noinspection PyShadowingBuiltins
def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class Binary:
    api: BinaryAPI

    def __init__(self, app_id, token, message_callback=None):
        self.app_id = app_id
        self.token = token

        self.message_callback = message_callback

        self.max_reconnect = 5
        self.connect_count = 0
        self.suspend = 0.5

        self.connect()

    def connect(self):
        while True:
            try:
                self.api.close()
            except Exception:
                pass
                # logging.error('**warning** self.api.close() fail')
            if self.connect_count < self.max_reconnect or self.max_reconnect < 0:
                self.api = BinaryAPI(self.app_id, self.token)
                self.api.message_callback = self.message_callback
                check = None

                check = self.api.connect()

                if check:
                    self.api.balance(subscribe=True)
                    self.api.transaction(subscribe=True)
                    break

                time.sleep(self.suspend * 2)
                self.connect_count = self.connect_count + 1
            else:
                logging.error(
                    '**error** reconnect() too many time please look log file')

    # buy_call_put
    # TODO buy_higher_lower
    def buy_call_put(self, contract_type, amount, symbol, duration, duration_unit, min_payout=0, passthrough=None,
                     req_id=None, instant=False, is_async=False):

        buy_id = None
        parameters = None
        if instant:
            parameters = dict(symbol=symbol, duration=duration, duration_unit=duration_unit,
                              basis=OP_code.PROPOSAL_BASIS.STAKE, amount=amount, currency=self.api.profile.currency, )
        else:
            prop_req_id = self.api.proposal(contract_type=contract_type, symbol=symbol, duration_unit=duration_unit,
                                            duration=duration, amount=amount)
            start_t = time.time()
            while self.api.msg_by_req_id.get(prop_req_id) is None:
                if time.time() - start_t >= 30:
                    logging.error('**warning** proposal late 30 sec')
                    return False, None, prop_req_id

            proposal_res = self.api.msg_by_req_id[prop_req_id]
            if 'error' in proposal_res:
                return False, None, prop_req_id
            # min_payout
            proposal_obj = proposal_res['proposal']
            payout = (proposal_obj['payout'] - proposal_obj['ask_price']) / proposal_obj['ask_price'] * 100
            if payout >= min_payout:
                buy_id = proposal_obj['id']
            else:
                return False, None, prop_req_id

        req_id = self.api.buy(buy_id=buy_id, max_price=amount, parameters=parameters, passthrough=passthrough, req_id=req_id)

        if is_async:
            return True, None, req_id
        else:
            start_t = time.time()
            while self.api.msg_by_type['buy'].get(req_id) is None:
                if time.time() - start_t >= 30:
                    logging.error('**warning** buy late 30 sec')
                    return False, None, req_id

            res = self.api.msg_by_type['buy'][req_id]
            if 'error' in res:
                return False, None, req_id

            # TODO
            return True, res['buy']['contract_id'], req_id

    buy = buy_call_put
