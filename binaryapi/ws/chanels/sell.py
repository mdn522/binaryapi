"""Module for Binary sell websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union
from decimal import Decimal


# https://developers.binary.com/api/#sell

class Sell(Base):
    """Class for Binary sell websocket channel."""

    name = "sell"

    def __call__(self, sell: int, price: Union[int, float, Decimal], passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to sell websocket channel.
        Sell Contract (request)
        Sell a Contract as identified from a previous `portfolio` call.
        :param sell: Pass contract_id received from the `portfolio` call.
        :type sell: int
        :param price: Minimum price at which to sell the contract, or `0` for 'sell at market'.
        :type price: Union[int, float, Decimal]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "sell": int(sell),
            "price": price
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
