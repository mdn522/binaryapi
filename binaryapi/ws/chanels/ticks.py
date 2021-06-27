"""Module for Binary ticks websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Union, Any, Optional


# https://developers.binary.com/api/#ticks

class Ticks(Base):
    """Class for Binary ticks websocket channel."""

    name = "ticks"

    def __call__(self, ticks, subscribe: Union[bool, int, None] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to ticks websocket channel.
        Ticks Stream (request)
        Initiate a continuous stream of spot price updates for a given symbol.
        :param ticks: The short symbol name or array of symbols (obtained from `active_symbols` call).
        :type ticks: 
        :param subscribe: [Optional] If set to 1, will send updates whenever a new tick is received.
        :type subscribe: Union[bool, int, None]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "ticks": ticks
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
