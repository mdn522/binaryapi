"""Module for Binary mt5_password_change websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#mt5_password_change

class Mt5PasswordChange(Base):
    """Class for Binary mt5_password_change websocket channel."""

    name = "mt5_password_change"

    def __call__(
        self, 
        login: str, 
        new_password: str, 
        old_password: str, 
        password_type: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to mt5_password_change websocket channel.
        MT5: Password Change (request)
        To change passwords of the MT5 account.

        :param login: MT5 user login
        :type login: str
        :param new_password: New password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
        :type new_password: str
        :param old_password: Old password for validation (non-empty string, accepts any printable ASCII character)
        :type old_password: str
        :param password_type: [Optional] Type of the password to change.
        :type password_type: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "mt5_password_change": int(1),
            "login": login,
            "new_password": new_password,
            "old_password": old_password
        }

        if password_type:
            data['password_type'] = str(password_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
