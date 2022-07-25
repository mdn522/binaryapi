"""Module for Binary p2p_order_dispute websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_order_dispute

class P2POrderDispute(Base):
    """Class for Binary p2p_order_dispute websocket channel."""

    name = "p2p_order_dispute"

    def __call__(
        self, 
        dispute_reason: str, 
        id: str, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_order_dispute websocket channel.
        P2P Order Dispute (request)
        Dispute a P2P order.

        :param dispute_reason: The predefined dispute reason
        :type dispute_reason: str
        :param id: The unique identifier for this order.
        :type id: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_order_dispute": int(1),
            "dispute_reason": dispute_reason,
            "id": id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
