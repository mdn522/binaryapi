"""Module for Binary contract_update websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#contract_update

class ContractUpdate(Base):
    """Class for Binary contract_update websocket chanel."""

    name = "contract_update"

    def __call__(self, contract_id: int, limit_order, passthrough=None, req_id: int = None):
        """Method to send message to contract_update websocket chanel.
        Update Contract (request)
        Update a contract condition.
        :param contract_id: Internal unique contract identifier.
        :type contract_id: int
        :param limit_order: Specify limit order to update.
        :type limit_order: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "contract_update": 1,
            "contract_id": contract_id,
            "limit_order": limit_order
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
