"""Module for Binary mt5_password_reset websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#mt5_password_reset

class Mt5PasswordReset(Base):
    """Class for Binary mt5_password_reset websocket chanel."""

    name = "mt5_password_reset"

    def __call__(self, login: str, new_password: str, verification_code: str, password_type: str=None, passthrough=None, req_id: int=None):
        """Method to send message to mt5_password_reset websocket chanel.
        MT5: Password Reset (request)
        To reset the password of MT5 account.
        :param login: MT5 user login
        :type login: str
        :param new_password: New password of the account. For validation (length within 8-25 chars, accepts at least 2 out of the following 3 types of characters: uppercase letters, lowercase letters, and numbers).
        :type new_password: str
        :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
        :type verification_code: str
        :param password_type: [Optional] Type of the password to reset.
        :type password_type: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "mt5_password_reset": 1,
            "login": login,
            "new_password": new_password,
            "verification_code": verification_code
        }

        if password_type:
            data['password_type'] = password_type

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
