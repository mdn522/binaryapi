"""Module for Binary app_delete websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#app_delete

class AppDelete(Base):
    """Class for Binary app_delete websocket channel."""

    name = "app_delete"

    def __call__(
        self, 
        app_delete: int, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to app_delete websocket channel.
        Application: Delete (request)
        The request for deleting an application.

        :param app_delete: Application app_id
        :type app_delete: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "app_delete": int(app_delete)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
