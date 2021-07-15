"""Module for Binary mt5_login_list websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#mt5_login_list

class Mt5LoginList(Base):
    """Class for Binary mt5_login_list websocket channel."""

    name = "mt5_login_list"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to mt5_login_list websocket channel.
        MT5: Accounts List (request)
        Get list of MT5 accounts for client
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "mt5_login_list": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
