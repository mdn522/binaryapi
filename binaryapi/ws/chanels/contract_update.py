"""Module for Binary contract_update websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#contract_update

class ContractUpdate(Base):
    """Class for Binary contract_update websocket channel."""

    name = "contract_update"

    def __call__(
        self, 
        contract_id: int, 
        limit_order, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to contract_update websocket channel.
        Update Contract (request)
        Update a contract condition.

        :param contract_id: Internal unique contract identifier.
        :type contract_id: int
        :param limit_order: Specify limit order to update.
        :type limit_order: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "contract_update": int(1),
            "contract_id": int(contract_id),
            "limit_order": limit_order
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
