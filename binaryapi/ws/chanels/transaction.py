"""Module for Binary transaction websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#transaction

class Transaction(Base):
    """Class for Binary transaction websocket chanel."""

    name = "transaction"

    def __call__(self, subscribe: bool, passthrough=None, req_id: int=None):
        """Method to send message to transaction websocket chanel.
        Transactions Stream (request)
        Subscribe to transaction notifications
        :param subscribe: If set to 1, will send updates whenever there is an update to transactions. If not to 1 then it will not return any records.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "transaction": 1,
            "subscribe": subscribe
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
