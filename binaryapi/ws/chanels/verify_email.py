"""Module for Binary verify_email websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#verify_email

class VerifyEmail(Base):
    """Class for Binary verify_email websocket chanel."""

    name = "verify_email"

    def __call__(self, verify_email: str, type: str, url_parameters=None, passthrough=None, req_id: int=None):
        """Method to send message to verify_email websocket chanel.
        Verify Email (request)
        Verify an email address for various purposes. The system will send an email to the address containing a security code for verification.
        :param verify_email: Email address to be verified.
        :type verify_email: str
        :param type: Purpose of the email verification call.
        :type type: str
        :param url_parameters: [Optional] Extra parameters that can be attached to the verify email link URL.
        :type url_parameters: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "verify_email": verify_email,
            "type": type
        }

        if url_parameters:
            data['url_parameters'] = url_parameters

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
