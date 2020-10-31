"""Module for Binary mt5_get_settings websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#mt5_get_settings

class Mt5GetSettings(Base):
    """Class for Binary mt5_get_settings websocket channel."""

    name = "mt5_get_settings"

    def __call__(self, login: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to mt5_get_settings websocket channel.
        MT5: Get Setting (request)
        Get MT5 user account settings
        :param login: MT5 user login
        :type login: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "mt5_get_settings": int(1),
            "login": login
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
