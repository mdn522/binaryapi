"""Module for Binary buy_contract_for_multiple_accounts websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#buy_contract_for_multiple_accounts

class BuyContractForMultipleAccounts(Base):
    """Class for Binary buy_contract_for_multiple_accounts websocket chanel."""

    name = "buy_contract_for_multiple_accounts"

    def __call__(self, buy_contract_for_multiple_accounts: str, price, tokens, parameters=None, passthrough=None, req_id: int=None):
        """Method to send message to buy_contract_for_multiple_accounts websocket chanel.
        Buy Contract for Multiple Accounts (request)
        Buy a Contract for multiple Accounts specified by the `tokens` parameter. Note, although this is an authorized call, the contract is not bought for the authorized account.
        :param buy_contract_for_multiple_accounts: Either the ID received from a Price Proposal (`proposal` call), or `1` if contract buy parameters are passed in the `parameters` field.
        :type buy_contract_for_multiple_accounts: str
        :param price: Maximum price at which to purchase the contract.
        :type price: 
        :param tokens: List of API tokens identifying the accounts for which the contract is bought. Note: If the same token appears multiple times or if multiple tokens designate the same account, the contract is bought multiple times for this account.
        :type tokens: 
        :param parameters: [Optional] Used to pass the parameters for contract buy.
        :type parameters: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "buy_contract_for_multiple_accounts": buy_contract_for_multiple_accounts,
            "price": price,
            "tokens": tokens
        }

        if parameters:
            data['parameters'] = parameters

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
