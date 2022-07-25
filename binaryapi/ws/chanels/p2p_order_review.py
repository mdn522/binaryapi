"""Module for Binary p2p_order_review websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#p2p_order_review

class P2POrderReview(Base):
    """Class for Binary p2p_order_review websocket channel."""

    name = "p2p_order_review"

    def __call__(
        self, 
        order_id: str, 
        rating: int, 
        recommended: Optional[int] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_order_review websocket channel.
        P2P Order Review (request)
        Creates a review for the specified order.

        :param order_id: The order identification number.
        :type order_id: str
        :param rating: Rating for the transaction, 1 to 5.
        :type rating: int
        :param recommended: [Optional] `1` if the counterparty is recommendable to others, otherwise `0`.
        :type recommended: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_order_review": int(1),
            "order_id": order_id,
            "rating": int(rating)
        }

        if recommended:
            data['recommended'] = int(recommended)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
