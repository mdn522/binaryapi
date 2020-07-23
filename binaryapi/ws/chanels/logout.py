"""Module for Binary logout websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#logout

class Logout(Base):
    """Class for Binary logout websocket chanel."""

    name = "logout"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to logout websocket chanel.
        Log Out (request)
        Logout the session
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "logout": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
