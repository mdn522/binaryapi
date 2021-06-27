"""Module for Binary ping websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#ping

class Ping(Base):
    """Class for Binary ping websocket channel."""

    name = "ping"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to ping websocket channel.
        Ping (request)
        To send the ping request to the server. Mostly used to test the connection or to keep it alive.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "ping": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
