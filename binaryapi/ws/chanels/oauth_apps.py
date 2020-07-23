"""Module for Binary oauth_apps websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#oauth_apps

class OauthApps(Base):
    """Class for Binary oauth_apps websocket chanel."""

    name = "oauth_apps"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to oauth_apps websocket chanel.
        OAuth Applications (request)
        List all my used OAuth applications.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "oauth_apps": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
