"""Module for Binary mt5_deposit websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Union, Optional


# https://developers.binary.com/api/#mt5_deposit

class Mt5Deposit(Base):
    """Class for Binary mt5_deposit websocket channel."""

    name = "mt5_deposit"

    def __call__(self, to_mt5: str, amount: Optional[Union[int, float, Decimal]] = None, from_binary: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to mt5_deposit websocket channel.
        MT5: Deposit (request)
        This call allows deposit into MT5 account from Binary account.
        :param to_mt5: MT5 account login to deposit money to
        :type to_mt5: str
        :param amount: Amount to deposit (in the currency of from_binary); min = $1 or an equivalent amount, max = $20000 or an equivalent amount
        :type amount: Optional[Union[int, float, Decimal]]
        :param from_binary: Binary account loginid to transfer money from
        :type from_binary: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "mt5_deposit": int(1),
            "to_mt5": to_mt5
        }

        if amount:
            data['amount'] = amount

        if from_binary:
            data['from_binary'] = str(from_binary)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
