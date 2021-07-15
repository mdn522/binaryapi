"""Module for Binary p2p_order_confirm websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_order_confirm

class P2POrderConfirm(Base):
    """Class for Binary p2p_order_confirm websocket channel."""

    name = "p2p_order_confirm"

    def __call__(self, id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_order_confirm websocket channel.
        P2P Order Confirm (request)
        Confirm a P2P order. **This API call is still in Beta.**
        :param id: The unique identifier for this order.
        :type id: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_order_confirm": int(1),
            "id": id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
