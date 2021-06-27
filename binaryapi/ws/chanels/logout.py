"""Module for Binary logout websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#logout

class Logout(Base):
    """Class for Binary logout websocket channel."""

    name = "logout"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to logout websocket channel.
        Log Out (request)
        Logout the session
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "logout": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
