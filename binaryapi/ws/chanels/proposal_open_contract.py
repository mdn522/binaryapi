"""Module for Binary proposal_open_contract websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#proposal_open_contract

class ProposalOpenContract(Base):
    """Class for Binary proposal_open_contract websocket channel."""

    name = "proposal_open_contract"

    def __call__(
        self, 
        contract_id: Optional[int] = None, 
        subscribe: Optional[Union[bool, int]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to proposal_open_contract websocket channel.
        Price Proposal: Open Contracts (request)
        Get latest price (and other information) for a contract in the user's portfolio

        :param contract_id: [Optional] Contract ID received from a `portfolio` request. If not set, you will receive stream of all open contracts.
        :type contract_id: Optional[int]
        :param subscribe: [Optional] `1` to stream.
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "proposal_open_contract": int(1)
        }

        if contract_id:
            data['contract_id'] = int(contract_id)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
