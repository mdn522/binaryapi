"""Module for Binary payout_currencies websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#payout_currencies

class PayoutCurrencies(Base):
    """Class for Binary payout_currencies websocket channel."""

    name = "payout_currencies"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to payout_currencies websocket channel.
        Payout Currencies (request)
        Retrieve a list of available option payout currencies. If a user is logged in, only the currencies available for the account will be returned.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "payout_currencies": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
