"""Module for Binary website_status websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#website_status

class WebsiteStatus(Base):
    """Class for Binary website_status websocket channel."""

    name = "website_status"

    def __call__(self, subscribe: Union[bool, int, None] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to website_status websocket channel.
        Server Status (request)
        Request server status.
        :param subscribe: [Optional] `1` to stream the server/website status updates.
        :type subscribe: Union[bool, int, None]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "website_status": int(1)
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
