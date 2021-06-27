"""Module for Binary set_account_currency websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#set_account_currency

class SetAccountCurrency(Base):
    """Class for Binary set_account_currency websocket channel."""

    name = "set_account_currency"

    def __call__(self, set_account_currency: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to set_account_currency websocket channel.
        Set Account Currency (request)
        Set account currency, this will be default currency for your account i.e currency for trading, deposit. Please note that account currency can only be set once, and then can never be changed.
        :param set_account_currency: Currency of the account. List of supported currencies can be acquired with `payout_currencies` call.
        :type set_account_currency: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "set_account_currency": set_account_currency
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
