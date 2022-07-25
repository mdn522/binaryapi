"""Module for Binary mt5_password_check websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#mt5_password_check

class Mt5PasswordCheck(Base):
    """Class for Binary mt5_password_check websocket channel."""

    name = "mt5_password_check"

    def __call__(
        self, 
        login: str, 
        password: str, 
        password_type: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to mt5_password_check websocket channel.
        MT5: Password Check (request)
        This call validates the main password for the MT5 user

        :param login: MT5 user login
        :type login: str
        :param password: The password of the account.
        :type password: str
        :param password_type: [Optional] Type of the password to check.
        :type password_type: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "mt5_password_check": int(1),
            "login": login,
            "password": password
        }

        if password_type:
            data['password_type'] = str(password_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
