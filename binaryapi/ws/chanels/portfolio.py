"""Module for Binary portfolio websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional


# https://developers.binary.com/api/#portfolio

class Portfolio(Base):
    """Class for Binary portfolio websocket channel."""

    name = "portfolio"

    def __call__(self, contract_type: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to portfolio websocket channel.
        Portfolio (request)
        Receive information about my current portfolio of outstanding options
        :param contract_type: Return only contracts of the specified types
        :type contract_type: Optional[List]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "portfolio": int(1)
        }

        if contract_type:
            data['contract_type'] = contract_type

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
