"""Module for Binary p2p_payment_methods websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_payment_methods

class P2PPaymentMethods(Base):
    """Class for Binary p2p_payment_methods websocket channel."""

    name = "p2p_payment_methods"

    def __call__(
        self, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_payment_methods websocket channel.
        P2P Payment Methods (request)
        List all P2P payment methods.

        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_payment_methods": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
