"""Module for Binary forget websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#forget

class Forget(Base):
    """Class for Binary forget websocket channel."""

    name = "forget"

    def __call__(
        self, 
        forget: str, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to forget websocket channel.
        Forget (request)
        Immediately cancel the real-time stream of messages with a specific ID.

        :param forget: ID of the real-time stream of messages to cancel.
        :type forget: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "forget": forget
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
