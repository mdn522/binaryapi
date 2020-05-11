"""Module for Binary ticks websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#ticks

class Ticks(Base):
    """Class for Binary ticks websocket chanel."""

    name = "ticks"

    def __call__(self, ticks, subscribe: bool = None, passthrough=None, req_id: int = None):
        """Method to send message to ticks websocket chanel.
        Ticks Stream (request)
        Initiate a continuous stream of spot price updates for a given symbol.
        :param ticks: The short symbol name or array of symbols (obtained from `active_symbols` call).
        :type ticks: 
        :param subscribe: [Optional] If set to 1, will send updates whenever a new tick is received.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "ticks": ticks
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
