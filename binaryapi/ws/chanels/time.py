"""Module for Binary time websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#time

class Time(Base):
    """Class for Binary time websocket chanel."""

    name = "time"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to time websocket chanel.
        Server Time (request)
        Request back-end server epoch time.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "time": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
