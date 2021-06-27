"""Module for Binary get_settings websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#get_settings

class GetSettings(Base):
    """Class for Binary get_settings websocket channel."""

    name = "get_settings"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to get_settings websocket channel.
        Get Account Settings (request)
        Get User Settings (email, date of birth, address etc)
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "get_settings": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
