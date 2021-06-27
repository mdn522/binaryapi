"""Module for Binary transfer_between_accounts websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Union, Optional, Any
from decimal import Decimal


# https://developers.binary.com/api/#transfer_between_accounts

class TransferBetweenAccounts(Base):
    """Class for Binary transfer_between_accounts websocket channel."""

    name = "transfer_between_accounts"

    def __call__(self, account_from: Optional[str] = None, account_to: Optional[str] = None, accounts: Optional[str] = None, amount: Optional[Union[int, float, Decimal]] = None, currency: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to transfer_between_accounts websocket channel.
        Transfer Between Accounts (request)
        This call allows transfers between accounts held by a given user. Transfer funds between your fiat and cryptocurrency accounts (for a fee). Please note that account_from should be same as current authorized account.
        :param account_from: [Optional] The loginid of the account to transfer funds from.
        :type account_from: Optional[str]
        :param account_to: [Optional] The loginid of the account to transfer funds to.
        :type account_to: Optional[str]
        :param accounts: [Optional] To control the list of accounts returned when `account_from` or `account_to` is not provided. `brief` will only include financial trading accounts with account_type equal to `binary` and can be faster. `all` will include accounts with both `mt5` and `binary` account_type
        :type accounts: Optional[str]
        :param amount: [Optional] The amount to transfer.
        :type amount: Optional[Union[int, float, Decimal]]
        :param currency: [Optional] Currency code.
        :type currency: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "transfer_between_accounts": int(1)
        }

        if account_from:
            data['account_from'] = str(account_from)

        if account_to:
            data['account_to'] = str(account_to)

        if accounts:
            data['accounts'] = str(accounts)

        if amount:
            data['amount'] = amount

        if currency:
            data['currency'] = str(currency)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
