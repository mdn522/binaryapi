"""Module for Binary revoke_oauth_app websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#revoke_oauth_app

class RevokeOauthApp(Base):
    """Class for Binary revoke_oauth_app websocket chanel."""

    name = "revoke_oauth_app"

    def __call__(self, revoke_oauth_app: int, passthrough=None, req_id: int = None):
        """Method to send message to revoke_oauth_app websocket chanel.
        Revoke Oauth Application (request)
        Used for revoking access of particular app.
        :param revoke_oauth_app: The application ID to revoke.
        :type revoke_oauth_app: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "revoke_oauth_app": revoke_oauth_app
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
