"""Module for Binary copytrading_list websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#copytrading_list

class CopytradingList(Base):
    """Class for Binary copytrading_list websocket channel."""

    name = "copytrading_list"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to copytrading_list websocket channel.
        Copy Trading: List (request)
        Retrieves a list of active copiers and/or traders for Copy Trading
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "copytrading_list": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
