"""Module for Binary login_history websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#login_history

class LoginHistory(Base):
    """Class for Binary login_history websocket channel."""

    name = "login_history"

    def __call__(self, limit: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to login_history websocket channel.
        Login History (request)
        Retrieve a summary of login history for user.
        :param limit: [Optional] Apply limit to count of login history records.
        :type limit: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "login_history": int(1)
        }

        if limit:
            data['limit'] = int(limit)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
