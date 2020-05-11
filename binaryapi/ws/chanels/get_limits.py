"""Module for Binary get_limits websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#get_limits

class GetLimits(Base):
    """Class for Binary get_limits websocket chanel."""

    name = "get_limits"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to get_limits websocket chanel.
        Account Limits (request)
        Trading and Withdrawal Limits for a given user
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "get_limits": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
