"""Module for Binary buy websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Optional, Union, Any


# https://developers.binary.com/api/#buy

class Buy(Base):
    """Class for Binary buy websocket channel."""

    name = "buy"

    def __call__(self, buy: str, price: Union[int, float, Decimal], parameters=None, subscribe: Union[bool, int, None] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to buy websocket channel.
        Buy Contract (request)
        Buy a Contract
        :param buy: Either the ID received from a Price Proposal (`proposal` call), or `1` if contract buy parameters are passed in the `parameters` field.
        :type buy: str
        :param price: Maximum price at which to purchase the contract.
        :type price: Union[int, float, Decimal]
        :param parameters: [Optional] Used to pass the parameters for contract buy.
        :type parameters: 
        :param subscribe: [Optional] `1` to stream.
        :type subscribe: Union[bool, int, None]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "buy": buy,
            "price": price
        }

        if parameters:
            data['parameters'] = parameters

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
