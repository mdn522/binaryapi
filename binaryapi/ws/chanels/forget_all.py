"""Module for Binary forget_all websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#forget_all

class ForgetAll(Base):
    """Class for Binary forget_all websocket chanel."""

    name = "forget_all"

    def __call__(self, forget_all, passthrough=None, req_id: int=None):
        """Method to send message to forget_all websocket chanel.
        Forget All (request)
        Immediately cancel the real-time streams of messages of given type.
        :param forget_all: Cancel all streams by type. The value can be either a single type e.g. `"ticks"`, or an array of multiple types e.g. `["candles", "ticks"]`.
        :type forget_all: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "forget_all": forget_all
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
