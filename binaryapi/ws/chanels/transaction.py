"""Module for Binary transaction websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#transaction

class Transaction(Base):
    """Class for Binary transaction websocket channel."""

    name = "transaction"

    def __call__(
        self, 
        subscribe: Optional[Union[bool, int]], 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to transaction websocket channel.
        Transactions Stream (request)
        Subscribe to transaction notifications

        :param subscribe: If set to 1, will send updates whenever there is an update to transactions. If not to 1 then it will not return any records.
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "transaction": int(1),
            "subscribe": int(subscribe)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
