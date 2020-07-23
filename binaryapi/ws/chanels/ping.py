"""Module for Binary ping websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#ping

class Ping(Base):
    """Class for Binary ping websocket chanel."""

    name = "ping"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to ping websocket chanel.
        Ping (request)
        To send the ping request to the server. Mostly used to test the connection or to keep it alive.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "ping": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
