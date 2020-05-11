"""Module for Binary copy_stop websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#copy_stop

class CopyStop(Base):
    """Class for Binary copy_stop websocket chanel."""

    name = "copy_stop"

    def __call__(self, copy_stop: str, passthrough=None, req_id: int = None):
        """Method to send message to copy_stop websocket chanel.
        Copy Trading: Stop (request)
        Stop copy trader bets
        :param copy_stop: API tokens identifying the accounts which needs not to be copied
        :type copy_stop: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "copy_stop": copy_stop
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
