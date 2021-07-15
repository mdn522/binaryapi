"""Module for Binary trading_platform_password_reset websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#trading_platform_password_reset

class TradingPlatformPasswordReset(Base):
    """Class for Binary trading_platform_password_reset websocket channel."""

    name = "trading_platform_password_reset"

    def __call__(self, new_password: str, verification_code: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to trading_platform_password_reset websocket channel.
        Trading Platform: Password Reset (request)
        Reset the password of a Trading Platform Account
        :param new_password: New password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
        :type new_password: str
        :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
        :type verification_code: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "trading_platform_password_reset": int(1),
            "new_password": new_password,
            "verification_code": verification_code
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
