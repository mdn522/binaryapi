"""Module for Binary transfer_between_accounts websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#transfer_between_accounts

class TransferBetweenAccounts(Base):
    """Class for Binary transfer_between_accounts websocket chanel."""

    name = "transfer_between_accounts"

    def __call__(self, account_from: str = None, account_to: str = None, accounts: str = None, amount=None, currency: str = None, passthrough=None, req_id: int = None):
        """Method to send message to transfer_between_accounts websocket chanel.
        Transfer Between Accounts (request)
        This call allows transfers between accounts held by a given user. Transfer funds between your fiat and cryptocurrency accounts (for a fee). Please note that account_from should be same as current authorized account.
        :param account_from: [Optional] The loginid of the account to transfer funds from.
        :type account_from: str
        :param account_to: [Optional] The loginid of the account to transfer funds to.
        :type account_to: str
        :param accounts: [Optional] To control the list of accounts returned when `account_from` or `account_to` is not provided. `brief` will only include financial trading accounts with account_type equal to `binary` and can be faster. `all` will include accounts with both `mt5` and `binary` account_type
        :type accounts: str
        :param amount: [Optional] The amount to transfer.
        :type amount: 
        :param currency: [Optional] Currency code.
        :type currency: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
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
