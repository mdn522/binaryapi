"""Module for Binary contract_update_history websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#contract_update_history

class ContractUpdateHistory(Base):
    """Class for Binary contract_update_history websocket chanel."""

    name = "contract_update_history"

    def __call__(self, contract_id: int, passthrough=None, req_id: int=None):
        """Method to send message to contract_update_history websocket chanel.
        Update Contract History (request)
        Request for contract update history.
        :param contract_id: Internal unique contract identifier.
        :type contract_id: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "contract_update_history": 1,
            "contract_id": contract_id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
