"""Module for Binary portfolio websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#portfolio

class Portfolio(Base):
    """Class for Binary portfolio websocket chanel."""

    name = "portfolio"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to portfolio websocket chanel.
        Portfolio (request)
        Receive information about my current portfolio of outstanding options
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "portfolio": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
