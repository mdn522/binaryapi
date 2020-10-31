"""Module for Binary p2p_chat_create websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#p2p_chat_create

class P2PChatCreate(Base):
    """Class for Binary p2p_chat_create websocket channel."""

    name = "p2p_chat_create"

    def __call__(self, order_id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_chat_create websocket channel.
        P2P Chat Create (request)
        Creates a P2P chat for the specified order. **This API call is still in Beta.**
        :param order_id: The unique identifier for the order to create the chat for.
        :type order_id: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_chat_create": int(1),
            "order_id": order_id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
