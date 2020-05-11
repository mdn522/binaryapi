"""Module for Binary get_self_exclusion websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#get_self_exclusion

class GetSelfExclusion(Base):
    """Class for Binary get_self_exclusion websocket chanel."""

    name = "get_self_exclusion"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to get_self_exclusion websocket chanel.
        Get Self-Exclusion (request)
        Allows users to exclude themselves from the website for certain periods of time, or to set limits on their trading activities. This facility is a regulatory requirement for certain Landing Companies.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "get_self_exclusion": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
