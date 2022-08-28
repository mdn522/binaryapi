from typing import Optional, Union, Any, Tuple, Callable
from decimal import Decimal
import logging
import uuid
import pause

from binaryapi import global_value
from binaryapi import global_config
from binaryapi.api import BinaryAPI
from binaryapi.constants import PROPOSAL_BASIS
from binaryapi.exceptions import MessageByReqIDNotFound

# TODO support tick stream
DEFAULT_MAX_RECONNECT = 5
DEFAULT_SUSPEND = 0.5


class Binary:
    api: BinaryAPI

    # Global Value Unique ID
    gv_uid: str

    def __init__(self, token: str = None, app_id: int = None, message_callback: Optional[Callable] = None):
        self.app_id = app_id
        self.token = token

        self.message_callback = message_callback

        # TODO
        self.gv_uid = str(uuid.uuid4())

        self.max_reconnect = DEFAULT_MAX_RECONNECT
        self.connect_count = 0
        self.suspend = DEFAULT_SUSPEND

        self.connect()

    @property
    def message_callback(self):
        return self._message_callback

    @message_callback.setter
    def message_callback(self, value):
        self._message_callback = value
        try:
            self.api.message_callback = self._message_callback
        except AttributeError:
            pass

    @property
    def basic(self) -> BinaryAPI:
        return self.api

    @basic.setter
    def basic(self, value: BinaryAPI):
        self.api = value

    def connect(self):
        while True:
            # noinspection PyBroadException
            try:
                self.api.close()
            except Exception:
                pass
                # logging.error('**warning** self.api.close() fail')
            if self.connect_count < self.max_reconnect or self.max_reconnect < 0:
                self.api = BinaryAPI(token=self.token, app_id=self.app_id)
                # self.api.message_callback = self.message_callback

                self.api.message_callback = self.message_callback

                check = self.api.connect()

                if check:
                    if global_config.AUTO_SUBSCRIBE_TO_BALANCE_ON_CONNECT:
                        self.api.balance(subscribe=True)

                    if global_config.AUTO_SUBSCRIBE_TO_TRANSACTION_ON_CONNECT:
                        self.api.transaction(subscribe=True)

                    break

                pause.sleep(self.suspend * 2)
                self.connect_count = self.connect_count + 1
            else:
                logging.error('**error** reconnect() too many time please look log file')

            pause.sleep(0.001)

    @staticmethod
    def check_connect():
        return global_value.check_websocket_if_connect == 1

    # buy_call_put
    # TODO buy_higher_lower
    # TODO buy_through_proposal
    # TODO direct_buy
    def buy_call_put(
        self,
        contract_type: str,
        amount: Union[int, float, Decimal],
        symbol: str,
        duration,
        duration_unit: str,
        min_payout: Union[int, float, Decimal] = 0,
        basis=PROPOSAL_BASIS.STAKE,
        subscribe: Optional[bool] = None,
        passthrough: Optional[Any] = None,
        req_id: Optional[int] = None,
        no_proposal=False,
        confirm_request: bool = True
    ) -> Tuple[bool, Optional[str], Optional[int]]:
        """
        :rtype: Tuple[bool, Optional[str], Optional[int]]
        :desc: Tuple[success?, contract_id (if success), req_id]
        success: Is the request successful?
        contract_id: Contract ID if successful
        req_id: req_id for buy request if buy request is successful [OR] req_id for proposal request if buy request is not successful
        if confirm_request is false then contract_id will be none
        """
        buy_id = None
        parameters = None
        if no_proposal:
            parameters = dict(
                symbol=symbol,
                duration=duration,
                duration_unit=duration_unit,
                basis=PROPOSAL_BASIS.STAKE,
                amount=amount,
                currency=self.api.profile.currency,
            )
        else:
            prop_req_id = self.api.proposal(
                contract_type=contract_type,
                currency=self.api.profile.currency,
                symbol=symbol,
                duration_unit=duration_unit,
                duration=duration,
                amount=amount,
                basis=basis,
            )
            try:
                self.api.wait_for_response_by_req_id(req_id=prop_req_id, type_name='proposal')
            except MessageByReqIDNotFound:
                return False, None, prop_req_id

            proposal_res = self.api.msg_by_req_id[prop_req_id]
            if 'error' in proposal_res:
                return False, None, prop_req_id

            # min_payout
            proposal_obj = proposal_res['proposal']
            payout = (proposal_obj['payout'] - proposal_obj['ask_price']) / proposal_obj['ask_price'] * 100  # Current Payout in Percentage %
            if payout >= min_payout:
                buy_id = proposal_obj['id']
            else:
                return False, None, prop_req_id

        req_id = self.api.buy(buy=buy_id, price=amount, subscribe=subscribe, parameters=parameters, passthrough=passthrough, req_id=req_id)

        if not confirm_request:
            return True, None, req_id

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


Deriv = Binary
