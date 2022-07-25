"""Module for Binary revoke_oauth_app websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#revoke_oauth_app

class RevokeOauthApp(Base):
    """Class for Binary revoke_oauth_app websocket channel."""

    name = "revoke_oauth_app"

    def __call__(
        self, 
        revoke_oauth_app: int, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to revoke_oauth_app websocket channel.
        Revoke Oauth Application (request)
        Used for revoking access of particular app.

        :param revoke_oauth_app: The application ID to revoke.
        :type revoke_oauth_app: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "revoke_oauth_app": int(revoke_oauth_app)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
