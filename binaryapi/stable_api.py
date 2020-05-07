import sys

from binaryapi.api import BinaryAPI
import binaryapi.constants as OP_code
import threading
import time
import logging
import operator

from collections import defaultdict, OrderedDict
# from binaryapi.expiration import get_expiration_time, get_remaning_time
from datetime import datetime, timedelta


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class Binary:
    def __init__(self, app_id, token):
        self.app_id = app_id
        self.token = token

        self.max_reconnect = 5
        self.connect_count = 0
        self.suspend = 0.5

        self.connect()

    def connect(self):
        while True:
            try:
                self.api.close()
            except:
                pass
                # logging.error('**warning** self.api.close() fail')
            if self.connect_count < self.max_reconnect or self.max_reconnect < 0:
                self.api = BinaryAPI(self.app_id, self.token)
                check = None

                check = self.api.connect()

                if check == True:
                    break
                time.sleep(self.suspend * 2)
                self.connect_count = self.connect_count + 1
            else:
                logging.error(
                    '**error** reconnect() too many time please look log file')
                # exit(1) # TODO

    def buy(self, contract_type, amount, symbol, duration, duration_unit, min_payout=0, passthrough=None,
            request_id=None, instant=False, is_async=False):
        if instant:
            parameters = dict(symbol=symbol, duration=duration, duration_unit=duration_unit,
                              basis=OP_code.PROPOSAL_BASIS.STAKE, amount=amount, currency=self.api.profile.currency, )
            request_id = self.api.buy(buy_id=None, max_price=amount, parameters=parameters, passthrough=passthrough,
                                      request_id=request_id)
        else:
            prop_req_id = self.api.proposal(contract_type=contract_type, symbol=symbol, duration_unit=duration_unit,
                                            duration=duration, amount=amount)
            start_t = time.time()
            while self.api.msg_by_request_id.get(prop_req_id) is None:
                if time.time() - start_t >= 30:
                    logging.error('**warning** proposal late 30 sec')
                    return False, None, prop_req_id

            proposal_res = self.api.msg_by_request_id[prop_req_id]
            if 'error' in proposal_res:
                return False, None, prop_req_id

            payout = (proposal_res['proposal']['payout'] - proposal_res['proposal']['ask_price']) / proposal_res['proposal']['ask_price'] * 100
            if payout >= min_payout:
                request_id = self.api.buy(buy_id=proposal_res['proposal']['id'], max_price=amount, passthrough=passthrough, request_id=request_id)
            else:
                return False, None, prop_req_id

        if is_async:
            return True, None, request_id
        else:
            start_t = time.time()
            while self.api.msg_by_name['buy'].get(request_id) is None:
                if time.time() - start_t >= 30:
                    logging.error('**warning** buy late 30 sec')
                    return False, None, request_id

            res = self.api.msg_by_name['buy'][request_id]
            if 'error' in res:
                return False, None, request_id

            # TODO
            return True, res['buy']['contract_id'], request_id
