"""Module for Binary sell websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#sell

class Sell(Base):
    """Class for Binary sell websocket chanel."""

    name = "sell"

    def __call__(self, sell: int, price, passthrough=None, req_id: int = None):
        """Method to send message to sell websocket chanel.
        Sell Contract (request)
        Sell a Contract as identified from a previous `portfolio` call.
        :param sell: Pass contract_id received from the `portfolio` call.
        :type sell: int
        :param price: Minimum price at which to sell the contract, or `0` for 'sell at market'.
        :type price: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "sell": int(sell),
            "price": price
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
