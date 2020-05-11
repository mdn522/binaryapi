"""Module for Binary mt5_deposit websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#mt5_deposit

class Mt5Deposit(Base):
    """Class for Binary mt5_deposit websocket chanel."""

    name = "mt5_deposit"

    def __call__(self, to_mt5: str, amount=None, from_binary: str=None, passthrough=None, req_id: int=None):
        """Method to send message to mt5_deposit websocket chanel.
        MT5: Deposit (request)
        This call allows deposit into MT5 account from Binary account.
        :param to_mt5: MT5 account login to deposit money to
        :type to_mt5: str
        :param amount: Amount to deposit (in the currency of from_binary); min = $1 or an equivalent amount, max = $20000 or an equivalent amount
        :type amount: 
        :param from_binary: Binary account loginid to transfer money from
        :type from_binary: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "mt5_deposit": 1,
            "to_mt5": to_mt5
        }

        if amount:
            data['amount'] = amount

        if from_binary:
            data['from_binary'] = from_binary

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
