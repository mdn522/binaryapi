"""Module for Binary balance websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#balance

class Balance(Base):
    """Class for Binary balance websocket channel."""

    name = "balance"

    def __call__(
        self, 
        account: Optional[str] = None, 
        subscribe: Optional[Union[bool, int]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to balance websocket channel.
        Balance (request)
        Get user account balance

        :param account: [Optional] If set to `all`, return the balances of all accounts one by one; if set to `current`, return the balance of current account; if set as an account id, return the balance of that account.
        :type account: Optional[str]
        :param subscribe: [Optional] If set to 1, will send updates whenever the balance changes.
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "balance": int(1)
        }

        if account:
            data['account'] = str(account)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
