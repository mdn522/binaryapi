"""Module for Binary sell_contract_for_multiple_accounts websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, List, Union, Optional


# https://developers.binary.com/api/#sell_contract_for_multiple_accounts

class SellContractForMultipleAccounts(Base):
    """Class for Binary sell_contract_for_multiple_accounts websocket channel."""

    name = "sell_contract_for_multiple_accounts"

    def __call__(self, price: Union[int, float, Decimal], shortcode: str, tokens: List, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to sell_contract_for_multiple_accounts websocket channel.
        Sell Contracts: Multiple Accounts (request)
        Sell contracts for multiple accounts simultaneously. Uses the shortcode response from `buy_contract_for_multiple_accounts` to identify the contract, and authorisation tokens to select which accounts to sell those contracts on. Note that only the accounts identified by the tokens will be affected. This will not sell the contract on the currently-authorised account unless you include the token for the current account.
        :param price: Minimum price at which to sell the contract, or `0` for 'sell at market'.
        :type price: Union[int, float, Decimal]
        :param shortcode: An internal ID used to identify the contract which was originally bought. This is returned from the `buy` and `buy_contract_for_multiple_accounts` calls.
        :type shortcode: str
        :param tokens: Authorisation tokens which select the accounts to sell use for the affected accounts.
        :type tokens: List
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "sell_contract_for_multiple_accounts": int(1),
            "price": price,
            "shortcode": shortcode,
            "tokens": tokens
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
