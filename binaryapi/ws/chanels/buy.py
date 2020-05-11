"""Module for Binary buy websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#buy

class Buy(Base):
    """Class for Binary buy websocket chanel."""

    name = "buy"

    def __call__(self, buy: str, price, parameters=None, subscribe: bool = None, passthrough=None, req_id: int = None):
        """Method to send message to buy websocket chanel.
        Buy Contract (request)
        Buy a Contract
        :param buy: Either the ID received from a Price Proposal (`proposal` call), or `1` if contract buy parameters are passed in the `parameters` field.
        :type buy: str
        :param price: Maximum price at which to purchase the contract.
        :type price: 
        :param parameters: [Optional] Used to pass the parameters for contract buy.
        :type parameters: 
        :param subscribe: [Optional] `1` to stream.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
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
