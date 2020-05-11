"""Module for Binary mt5_new_account websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#mt5_new_account

class Mt5NewAccount(Base):
    """Class for Binary mt5_new_account websocket chanel."""

    name = "mt5_new_account"

    def __call__(self, account_type: str, email: str, leverage, mainPassword: str, name: str, address: str=None, city: str=None, company: str=None, country: str=None, dry_run: int=None, investPassword: str=None, mt5_account_type: str=None, phone: str=None, phonePassword: str=None, state: str=None, zipCode: str=None, passthrough=None, req_id: int=None):
        """Method to send message to mt5_new_account websocket chanel.
        MT5: New Account (request)
        This call creates new MT5 user, either demo or real money user.
        :param account_type: Account type
        :type account_type: str
        :param email: Email address
        :type email: str
        :param leverage: Client leverage (from 1 to 1000).
        :type leverage: 
        :param mainPassword: The master password of the account. For validation (length within 8-25 chars, accepts at least 2 out of the following 3 types of characters: uppercase letters, lowercase letters, and numbers). This field is required.
        :type mainPassword: str
        :param name: Client's name. The maximum length here is 101 characters.
        :type name: str
        :param address: [Optional] The address of the user. The maximum length of this address field is 128 characters.
        :type address: str
        :param city: [Optional] User's city of residence.
        :type city: str
        :param company: [Optional] Name of the client's company. The maximum length of the company name is 64 characters.
        :type company: str
        :param country: [Optional] 2-letter country code (value received from `residence_list` call).
        :type country: str
        :param dry_run: [Optional] If set to 1, only validation is performed.
        :type dry_run: int
        :param investPassword: [Optional] The investor password of the account. For validation (length within 8-25 chars, accepts at least 2 out of the following 3 types of characters: uppercase letters, lowercase letters, and numbers).
        :type investPassword: str
        :param mt5_account_type: [Optional] Standard: Variable spreads, High leverage. Advanced: Variable spreads, Medium Leverage, more products.
        :type mt5_account_type: str
        :param phone: [Optional] User's phone number.
        :type phone: str
        :param phonePassword: [Optional] The user's phone password.
        :type phonePassword: str
        :param state: [Optional] User's state (region) of residence.
        :type state: str
        :param zipCode: [Optional] User's zip code.
        :type zipCode: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "mt5_new_account": 1,
            "account_type": account_type,
            "email": email,
            "leverage": leverage,
            "mainPassword": mainPassword,
            "name": name
        }

        if address:
            data['address'] = address

        if city:
            data['city'] = city

        if company:
            data['company'] = company

        if country:
            data['country'] = country

        if dry_run:
            data['dry_run'] = dry_run

        if investPassword:
            data['investPassword'] = investPassword

        if mt5_account_type:
            data['mt5_account_type'] = mt5_account_type

        if phone:
            data['phone'] = phone

        if phonePassword:
            data['phonePassword'] = phonePassword

        if state:
            data['state'] = state

        if zipCode:
            data['zipCode'] = zipCode

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
