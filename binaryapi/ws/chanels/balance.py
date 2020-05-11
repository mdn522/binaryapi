"""Module for Binary balance websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#balance

class Balance(Base):
    """Class for Binary balance websocket chanel."""

    name = "balance"

    def __call__(self, account: str=None, subscribe: bool=None, passthrough=None, req_id: int=None):
        """Method to send message to balance websocket chanel.
        Balance (request)
        Get user account balance
        :param account: [Optional] If set to `all`, return the balances of all accounts one by one; if set to `current`, return the balance of current account; if set as an account id, return the balance of that account.
        :type account: str
        :param subscribe: [Optional] If set to 1, will send updates whenever the balance changes.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "balance": 1
        }

        if account:
            data['account'] = account

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
