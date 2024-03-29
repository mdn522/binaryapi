"""Module for Binary sell_expired websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#sell_expired

class SellExpired(Base):
    """Class for Binary sell_expired websocket channel."""

    name = "sell_expired"

    def __call__(
        self, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to sell_expired websocket channel.
        Sell Expired Contracts (request)
        This call will try to sell any expired contracts and return the number of sold contracts.

        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "sell_expired": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
