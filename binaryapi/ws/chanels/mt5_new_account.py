"""Module for Binary mt5_new_account websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Union, Optional, Any
from decimal import Decimal


# https://developers.binary.com/api/#mt5_new_account

class Mt5NewAccount(Base):
    """Class for Binary mt5_new_account websocket channel."""

    name = "mt5_new_account"

    def __call__(self, account_type: str, email: str, leverage: Union[int, float, Decimal], mainPassword: str, name: str, address: Optional[str] = None, city: Optional[str] = None, company: Optional[str] = None, country: Optional[str] = None, currency: Optional[str] = None, dry_run: Optional[int] = None, investPassword: Optional[str] = None, mt5_account_category: Optional[str] = None, mt5_account_type: Optional[str] = None, phone: Optional[str] = None, phonePassword: Optional[str] = None, state: Optional[str] = None, zipCode: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to mt5_new_account websocket channel.
        MT5: New Account (request)
        This call creates new MT5 user, either demo or real money user.
        :param account_type: Account type. If set to 'financial', setting 'mt5_account_type' is also required.
        :type account_type: str
        :param email: Email address
        :type email: str
        :param leverage: Client leverage (from 1 to 1000).
        :type leverage: Union[int, float, Decimal]
        :param mainPassword: The master password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address). This field is required.
        :type mainPassword: str
        :param name: Client's name. The maximum length here is 101 characters.
        :type name: str
        :param address: [Optional] The address of the user. The maximum length of this address field is 128 characters.
        :type address: Optional[str]
        :param city: [Optional] User's city of residence.
        :type city: Optional[str]
        :param company: [Optional] Name of the client's company. The maximum length of the company name is 64 characters.
        :type company: Optional[str]
        :param country: [Optional] 2-letter country code (value received from `residence_list` call).
        :type country: Optional[str]
        :param currency: [Optional] MT5 account currency, the default value will be the qualified account currency.
        :type currency: Optional[str]
        :param dry_run: [Optional] If set to 1, only validation is performed.
        :type dry_run: Optional[int]
        :param investPassword: [Optional] The investor password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
        :type investPassword: Optional[str]
        :param mt5_account_category: [Optional] To choose whether account is conventional or swap_free. Unavailable for financial_stp MT5_account_type
        :type mt5_account_category: Optional[str]
        :param mt5_account_type: [Optional] Financial: Variable spreads, High leverage. Financial STP: Variable spreads, Medium Leverage, more products. If 'account_type' set to 'financial', setting 'mt5_account_type' is also required.
        :type mt5_account_type: Optional[str]
        :param phone: [Optional] User's phone number.
        :type phone: Optional[str]
        :param phonePassword: [Optional] The user's phone password.
        :type phonePassword: Optional[str]
        :param state: [Optional] User's state (region) of residence.
        :type state: Optional[str]
        :param zipCode: [Optional] User's zip code.
        :type zipCode: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "mt5_new_account": int(1),
            "account_type": account_type,
            "email": email,
            "leverage": leverage,
            "mainPassword": mainPassword,
            "name": name
        }

        if address:
            data['address'] = str(address)

        if city:
            data['city'] = str(city)

        if company:
            data['company'] = str(company)

        if country:
            data['country'] = str(country)

        if currency:
            data['currency'] = str(currency)

        if dry_run:
            data['dry_run'] = int(dry_run)

        if investPassword:
            data['investPassword'] = str(investPassword)

        if mt5_account_category:
            data['mt5_account_category'] = str(mt5_account_category)

        if mt5_account_type:
            data['mt5_account_type'] = str(mt5_account_type)

        if phone:
            data['phone'] = str(phone)

        if phonePassword:
            data['phonePassword'] = str(phonePassword)

        if state:
            data['state'] = str(state)

        if zipCode:
            data['zipCode'] = str(zipCode)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
