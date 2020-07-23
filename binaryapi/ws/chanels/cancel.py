"""Module for Binary cancel websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#cancel

class Cancel(Base):
    """Class for Binary cancel websocket chanel."""

    name = "cancel"

    def __call__(self, cancel: int, passthrough=None, req_id: int = None):
        """Method to send message to cancel websocket chanel.
        Cancel a Contract (request)
        Cancel contract with contract id
        :param cancel: Value should be the `contract_id` which received from the `portfolio` call.
        :type cancel: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "cancel": int(cancel)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
