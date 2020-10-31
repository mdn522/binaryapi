"""Module for Binary topup_virtual websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#topup_virtual

class TopupVirtual(Base):
    """Class for Binary topup_virtual websocket channel."""

    name = "topup_virtual"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to topup_virtual websocket channel.
        Top Up Virtual-Money Account (request)
        When a virtual-money's account balance becomes low, it can be topped up using this call.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "topup_virtual": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
