"""Module for Binary contract_update_history websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#contract_update_history

class ContractUpdateHistory(Base):
    """Class for Binary contract_update_history websocket channel."""

    name = "contract_update_history"

    def __call__(
        self, 
        contract_id: int, 
        limit: Optional[Union[int, float, Decimal]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to contract_update_history websocket channel.
        Update Contract History (request)
        Request for contract update history.

        :param contract_id: Internal unique contract identifier.
        :type contract_id: int
        :param limit: [Optional] Maximum number of historical updates to receive.
        :type limit: Optional[Union[int, float, Decimal]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "contract_update_history": int(1),
            "contract_id": int(contract_id)
        }

        if limit:
            data['limit'] = limit

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
