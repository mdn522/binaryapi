"""Module for Binary cancel websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#cancel

class Cancel(Base):
    """Class for Binary cancel websocket channel."""

    name = "cancel"

    def __call__(
        self, 
        cancel: int, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to cancel websocket channel.
        Cancel a Contract (request)
        Cancel contract with contract id

        :param cancel: Value should be the `contract_id` which received from the `portfolio` call.
        :type cancel: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "cancel": int(cancel)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
