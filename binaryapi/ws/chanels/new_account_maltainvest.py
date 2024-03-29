"""Module for Binary new_account_maltainvest websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#new_account_maltainvest

class NewAccountMaltainvest(Base):
    """Class for Binary new_account_maltainvest websocket channel."""

    name = "new_account_maltainvest"

    def __call__(
        self, 
        accept_risk: int, 
        address_city: str, 
        address_line_1: str, 
        date_of_birth: str, 
        education_level: str, 
        employment_industry: str, 
        estimated_worth: str, 
        first_name: str, 
        income_source: str, 
        last_name: str, 
        net_income: str, 
        occupation: str, 
        residence: str, 
        salutation: str, 
        tax_identification_number: str, 
        tax_residence: str, 
        account_opening_reason: Optional[str] = None, 
        account_turnover: Optional[str] = None, 
        address_line_2: Optional[str] = None, 
        address_postcode: Optional[str] = None, 
        address_state: Optional[str] = None, 
        affiliate_token: Optional[str] = None, 
        binary_options_trading_experience: Optional[str] = None, 
        binary_options_trading_frequency: Optional[str] = None, 
        cfd_trading_experience: Optional[str] = None, 
        cfd_trading_frequency: Optional[str] = None, 
        citizen: Optional[str] = None, 
        client_type: Optional[str] = None, 
        currency: Optional[str] = None, 
        employment_status: Optional[str] = None, 
        forex_trading_experience: Optional[str] = None, 
        forex_trading_frequency: Optional[str] = None, 
        non_pep_declaration: Optional[int] = None, 
        other_instruments_trading_experience: Optional[str] = None, 
        other_instruments_trading_frequency: Optional[str] = None, 
        phone: Optional[str] = None, 
        place_of_birth: Optional[str] = None, 
        secret_answer: Optional[str] = None, 
        secret_question: Optional[str] = None, 
        source_of_wealth: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to new_account_maltainvest websocket channel.
        New Real-Money Account: Deriv Investment (Europe) Ltd (request)
        This call opens a new real-money account with the `maltainvest` Landing Company. This call can be made from a virtual-money account or real-money account at Deriv (Europe) Limited. If it is the latter, client information fields in this call will be ignored and data from your existing real-money account will be used.

        :param accept_risk: Show whether client has accepted risk disclaimer.
        :type accept_risk: int
        :param address_city: Within 100 characters
        :type address_city: str
        :param address_line_1: Within 70 characters, with no leading whitespaces and may contain letters/numbers and/or any of following characters '.,:;()@#/-
        :type address_line_1: str
        :param date_of_birth: Date of birth format: yyyy-mm-dd.
        :type date_of_birth: str
        :param education_level: Level of Education
        :type education_level: str
        :param employment_industry: Industry of Employment.
        :type employment_industry: str
        :param estimated_worth: Estimated Net Worth.
        :type estimated_worth: str
        :param first_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type first_name: str
        :param income_source: Income Source.
        :type income_source: str
        :param last_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type last_name: str
        :param net_income: Net Annual Income.
        :type net_income: str
        :param occupation: Occupation.
        :type occupation: str
        :param residence: 2-letter country code, possible value receive from `residence_list` call.
        :type residence: str
        :param salutation: Accept any value in enum list.
        :type salutation: str
        :param tax_identification_number: Tax identification number. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_identification_number: str
        :param tax_residence: Residence for tax purpose. Comma separated iso country code if multiple jurisdictions. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_residence: str
        :param account_opening_reason: [Optional] Purpose and reason for requesting the account opening.
        :type account_opening_reason: Optional[str]
        :param account_turnover: [Optional] The anticipated account turnover.
        :type account_turnover: Optional[str]
        :param address_line_2: [Optional] Within 70 characters.
        :type address_line_2: Optional[str]
        :param address_postcode: [Optional] Within 20 characters and may not contain '+'.
        :type address_postcode: Optional[str]
        :param address_state: [Optional] Possible value receive from `states_list` call.
        :type address_state: Optional[str]
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: Optional[str]
        :param binary_options_trading_experience: [Optional] Binary options trading experience.
        :type binary_options_trading_experience: Optional[str]
        :param binary_options_trading_frequency: [Optional] Binary options trading frequency.
        :type binary_options_trading_frequency: Optional[str]
        :param cfd_trading_experience: [Optional] CFDs trading experience.
        :type cfd_trading_experience: Optional[str]
        :param cfd_trading_frequency: [Optional] CFDs trading frequency.
        :type cfd_trading_frequency: Optional[str]
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code. Possible value receive from `residence_list` call.
        :type citizen: Optional[str]
        :param client_type: [Optional] Indicates whether this is for a client requesting an account with professional status.
        :type client_type: Optional[str]
        :param currency: [Optional] To set currency of the account. List of supported currencies can be acquired with `payout_currencies` call.
        :type currency: Optional[str]
        :param employment_status: [Optional] Employment Status.
        :type employment_status: Optional[str]
        :param forex_trading_experience: [Optional] Forex trading experience.
        :type forex_trading_experience: Optional[str]
        :param forex_trading_frequency: [Optional] Forex trading frequency.
        :type forex_trading_frequency: Optional[str]
        :param non_pep_declaration: [Optional] Indicates client's self-declaration of not being a PEP/RCA.
        :type non_pep_declaration: Optional[int]
        :param other_instruments_trading_experience: [Optional] Trading experience in other financial instruments.
        :type other_instruments_trading_experience: Optional[str]
        :param other_instruments_trading_frequency: [Optional] Trading frequency in other financial instruments.
        :type other_instruments_trading_frequency: Optional[str]
        :param phone: [Optional] Starting with `+` followed by 9-35 digits, hyphens or space.
        :type phone: Optional[str]
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: Optional[str]
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters.
        :type secret_answer: Optional[str]
        :param secret_question: [Optional] Accept any value in enum list.
        :type secret_question: Optional[str]
        :param source_of_wealth: [Optional] Source of wealth.
        :type source_of_wealth: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "new_account_maltainvest": int(1),
            "accept_risk": int(accept_risk),
            "address_city": address_city,
            "address_line_1": address_line_1,
            "date_of_birth": date_of_birth,
            "education_level": education_level,
            "employment_industry": employment_industry,
            "estimated_worth": estimated_worth,
            "first_name": first_name,
            "income_source": income_source,
            "last_name": last_name,
            "net_income": net_income,
            "occupation": occupation,
            "residence": residence,
            "salutation": salutation,
            "tax_identification_number": tax_identification_number,
            "tax_residence": tax_residence
        }

        if account_opening_reason:
            data['account_opening_reason'] = str(account_opening_reason)

        if account_turnover:
            data['account_turnover'] = str(account_turnover)

        if address_line_2:
            data['address_line_2'] = str(address_line_2)

        if address_postcode:
            data['address_postcode'] = str(address_postcode)

        if address_state:
            data['address_state'] = str(address_state)

        if affiliate_token:
            data['affiliate_token'] = str(affiliate_token)

        if binary_options_trading_experience:
            data['binary_options_trading_experience'] = str(binary_options_trading_experience)

        if binary_options_trading_frequency:
            data['binary_options_trading_frequency'] = str(binary_options_trading_frequency)

        if cfd_trading_experience:
            data['cfd_trading_experience'] = str(cfd_trading_experience)

        if cfd_trading_frequency:
            data['cfd_trading_frequency'] = str(cfd_trading_frequency)

        if citizen:
            data['citizen'] = str(citizen)

        if client_type:
            data['client_type'] = str(client_type)

        if currency:
            data['currency'] = str(currency)

        if employment_status:
            data['employment_status'] = str(employment_status)

        if forex_trading_experience:
            data['forex_trading_experience'] = str(forex_trading_experience)

        if forex_trading_frequency:
            data['forex_trading_frequency'] = str(forex_trading_frequency)

        if non_pep_declaration:
            data['non_pep_declaration'] = int(non_pep_declaration)

        if other_instruments_trading_experience:
            data['other_instruments_trading_experience'] = str(other_instruments_trading_experience)

        if other_instruments_trading_frequency:
            data['other_instruments_trading_frequency'] = str(other_instruments_trading_frequency)

        if phone:
            data['phone'] = str(phone)

        if place_of_birth:
            data['place_of_birth'] = str(place_of_birth)

        if secret_answer:
            data['secret_answer'] = str(secret_answer)

        if secret_question:
            data['secret_question'] = str(secret_question)

        if source_of_wealth:
            data['source_of_wealth'] = str(source_of_wealth)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
