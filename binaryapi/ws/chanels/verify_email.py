"""Module for Binary verify_email websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#verify_email

class VerifyEmail(Base):
    """Class for Binary verify_email websocket channel."""

    name = "verify_email"

    def __call__(
        self, 
        verify_email: str, 
        type: str, 
        url_parameters=None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to verify_email websocket channel.
        Verify Email (request)
        Verify an email address for various purposes. The system will send an email to the address containing a security code for verification.

        :param verify_email: Email address to be verified.
        :type verify_email: str
        :param type: Purpose of the email verification call.
        :type type: str
        :param url_parameters: [Optional] Extra parameters that can be attached to the verify email link URL.
        :type url_parameters: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "verify_email": verify_email,
            "type": type
        }

        if url_parameters:
            data['url_parameters'] = url_parameters

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
