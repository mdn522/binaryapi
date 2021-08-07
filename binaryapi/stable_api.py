from decimal import Decimal
from typing import Optional, Union, Any, Tuple

from binaryapi import global_value
from binaryapi.api import BinaryAPI
# noinspection PyPep8Naming
# import binaryapi.constants as CONSTANTS
import time
import logging

from collections import defaultdict


# TODO support tick stream


# noinspection PyShadowingBuiltins
from binaryapi.constants import PROPOSAL_BASIS
from binaryapi.exceptions import MessageByReqIDNotFound


# noinspection PyShadowingBuiltins
def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class Binary:
    api: BinaryAPI

    def __init__(self, token=None, app_id=28035, message_callback=None):
        self.app_id = app_id
        self.token = token

        self.message_callback = message_callback

        self.max_reconnect = 5
        self.connect_count = 0
        self.suspend = 0.5

        self.connect()

    @property
    def message_callback(self):
        return self._message_callback

    @message_callback.setter
    def message_callback(self, value):
        self._message_callback = value
        try:
            self.api.message_callback = self._message_callback
        except:
            pass

    def connect(self):
        while True:
            # noinspection PyBroadException
            try:
                self.api.close()
            except Exception:
                pass
                # logging.error('**warning** self.api.close() fail')
            if self.connect_count < self.max_reconnect or self.max_reconnect < 0:
                self.api = BinaryAPI(self.app_id, self.token)
                # self.api.message_callback = self.message_callback

                self.api.message_callback = self.message_callback

                check = self.api.connect()

                if check:
                    self.api.balance(subscribe=True)
                    self.api.transaction(subscribe=True)
                    break

                time.sleep(self.suspend * 2)
                self.connect_count = self.connect_count + 1
            else:
                logging.error('**error** reconnect() too many time please look log file')

            time.sleep(0.001)

    @staticmethod
    def check_connect():
        return global_value.check_websocket_if_connect == 1

    # buy_call_put
    # TODO buy_higher_lower
    # TODO buy_through_proposal
    # TODO direct_buy
    def buy_call_put(self, contract_type: str, amount: Union[int, float, Decimal], symbol: str, duration, duration_unit, min_payout=0,
                     basis=PROPOSAL_BASIS.STAKE, subscribe: Optional[bool] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None, no_proposal=False,
                     confirm_request: bool = True) -> Tuple[bool, Optional[str], Optional[int]]:
        """
        :rtype: Tuple[bool, Optional[str], Optional[int]]
        :desc: Tuple[success, contract_id (if success), req_id]
        """
        buy_id = None
        parameters = None
        if no_proposal:
            parameters = dict(symbol=symbol, duration=duration, duration_unit=duration_unit,
                              basis=PROPOSAL_BASIS.STAKE, amount=amount, currency=self.api.profile.currency, )
        else:
            prop_req_id = self.api.proposal(contract_type=contract_type, currency=self.api.profile.currency,
                                            symbol=symbol, duration_unit=duration_unit,
                                            duration=duration, amount=amount, basis=basis)
            # start_t = time.time()
            # while self.api.msg_by_req_id.get(prop_req_id) is None:
            #     if time.time() - start_t >= 30:
            #         logging.error('**warning** proposal late 30 sec')
            #         return False, None, prop_req_id
            #     time.sleep(0.0005)

            try:
                self.api.wait_for_response_by_req_id(req_id=prop_req_id, type_name='proposal')
            except MessageByReqIDNotFound:
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

        req_id = self.api.buy(buy=buy_id, price=amount, subscribe=subscribe, parameters=parameters, passthrough=passthrough, req_id=req_id)

        if not confirm_request:
            return True, None, req_id
        else:
            # start_t = time.time()
            # while self.api.msg_by_type['buy'].get(req_id) is None:
            #     if time.time() - start_t >= 30:
            #         logging.error('**warning** buy late 30 sec')
            #         return False, None, req_id
            #     time.sleep(0.0005)

            try:
                self.api.wait_for_response_by_req_id(req_id=req_id, type='buy')
            except MessageByReqIDNotFound:
                return False, None, req_id

            res = self.api.msg_by_type['buy'][req_id]
            if 'error' in res:
                return False, None, req_id

            # TODO
            return True, res['buy']['contract_id'], req_id

    buy = buy_call_put
