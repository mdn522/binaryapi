"""Module for Binary app_get websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#app_get

class AppGet(Base):
    """Class for Binary app_get websocket channel."""

    name = "app_get"

    def __call__(
        self, 
        app_get: int, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to app_get websocket channel.
        Application: Get Details (request)
        To get the information of the OAuth application specified by 'app_id'

        :param app_get: Application app_id
        :type app_get: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "app_get": int(app_get)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
