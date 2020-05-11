"""Module for Binary new_account_maltainvest websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#new_account_maltainvest

class NewAccountMaltainvest(Base):
    """Class for Binary new_account_maltainvest websocket chanel."""

    name = "new_account_maltainvest"

    def __call__(self, accept_risk: int, address_city: str, address_line_1: str, date_of_birth: str, education_level: str, employment_industry: str, estimated_worth: str, first_name: str, income_source: str, last_name: str, net_income: str, occupation: str, residence: str, salutation: str, tax_identification_number: str, tax_residence: str, account_opening_reason: str=None, account_turnover: str=None, address_line_2: str=None, address_postcode: str=None, address_state: str=None, affiliate_token: str=None, binary_options_trading_experience: str=None, binary_options_trading_frequency: str=None, cfd_trading_experience: str=None, cfd_trading_frequency: str=None, citizen: str=None, client_type: str=None, employment_status: str=None, forex_trading_experience: str=None, forex_trading_frequency: str=None, non_pep_declaration: int=None, other_instruments_trading_experience: str=None, other_instruments_trading_frequency: str=None, phone: str=None, place_of_birth: str=None, secret_answer: str=None, secret_question: str=None, source_of_wealth: str=None, passthrough=None, req_id: int=None):
        """Method to send message to new_account_maltainvest websocket chanel.
        New Real-Money Account: Binary Investment (Europe) Ltd. (request)
        This call opens a new real-money account with the `maltainvest` Landing Company. This call can be made from a virtual-money account or real-money account at Binary (Europe) Ltd. If it is the latter, client information fields in this call will be ignored and data from your existing real-money account will be used.
        :param accept_risk: Show whether client has accepted risk disclaimer.
        :type accept_risk: int
        :param address_city: Within 35 characters
        :type address_city: str
        :param address_line_1: Within 70 characters.
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
        :type account_opening_reason: str
        :param account_turnover: [Optional] The anticipated account turnover.
        :type account_turnover: str
        :param address_line_2: [Optional] Within 70 characters.
        :type address_line_2: str
        :param address_postcode: [Optional] Within 20 characters and may not contain '+'.
        :type address_postcode: str
        :param address_state: [Optional] Possible value receive from `states_list` call.
        :type address_state: str
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: str
        :param binary_options_trading_experience: [Optional] Binary options trading experience.
        :type binary_options_trading_experience: str
        :param binary_options_trading_frequency: [Optional] Binary options trading frequency.
        :type binary_options_trading_frequency: str
        :param cfd_trading_experience: [Optional] CFDs trading experience.
        :type cfd_trading_experience: str
        :param cfd_trading_frequency: [Optional] CFDs trading frequency.
        :type cfd_trading_frequency: str
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code. Possible value receive from `residence_list` call.
        :type citizen: str
        :param client_type: [Optional] Indicates whether this is for a client requesting an account with professional status.
        :type client_type: str
        :param employment_status: [Optional] Employment Status.
        :type employment_status: str
        :param forex_trading_experience: [Optional] Forex trading experience.
        :type forex_trading_experience: str
        :param forex_trading_frequency: [Optional] Forex trading frequency.
        :type forex_trading_frequency: str
        :param non_pep_declaration: [Optional] Indicates client's self-declaration of not being a PEP/RCA.
        :type non_pep_declaration: int
        :param other_instruments_trading_experience: [Optional] Trading experience in other financial instruments.
        :type other_instruments_trading_experience: str
        :param other_instruments_trading_frequency: [Optional] Trading frequency in other financial instruments.
        :type other_instruments_trading_frequency: str
        :param phone: [Optional] Starting with `+` followed by 8-35 digits, allowing hyphens or space.
        :type phone: str
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: str
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters.
        :type secret_answer: str
        :param secret_question: [Optional] Accept any value in enum list.
        :type secret_question: str
        :param source_of_wealth: [Optional] Source of wealth.
        :type source_of_wealth: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "new_account_maltainvest": 1,
            "accept_risk": accept_risk,
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
            data['account_opening_reason'] = account_opening_reason

        if account_turnover:
            data['account_turnover'] = account_turnover

        if address_line_2:
            data['address_line_2'] = address_line_2

        if address_postcode:
            data['address_postcode'] = address_postcode

        if address_state:
            data['address_state'] = address_state

        if affiliate_token:
            data['affiliate_token'] = affiliate_token

        if binary_options_trading_experience:
            data['binary_options_trading_experience'] = binary_options_trading_experience

        if binary_options_trading_frequency:
            data['binary_options_trading_frequency'] = binary_options_trading_frequency

        if cfd_trading_experience:
            data['cfd_trading_experience'] = cfd_trading_experience

        if cfd_trading_frequency:
            data['cfd_trading_frequency'] = cfd_trading_frequency

        if citizen:
            data['citizen'] = citizen

        if client_type:
            data['client_type'] = client_type

        if employment_status:
            data['employment_status'] = employment_status

        if forex_trading_experience:
            data['forex_trading_experience'] = forex_trading_experience

        if forex_trading_frequency:
            data['forex_trading_frequency'] = forex_trading_frequency

        if non_pep_declaration:
            data['non_pep_declaration'] = non_pep_declaration

        if other_instruments_trading_experience:
            data['other_instruments_trading_experience'] = other_instruments_trading_experience

        if other_instruments_trading_frequency:
            data['other_instruments_trading_frequency'] = other_instruments_trading_frequency

        if phone:
            data['phone'] = phone

        if place_of_birth:
            data['place_of_birth'] = place_of_birth

        if secret_answer:
            data['secret_answer'] = secret_answer

        if secret_question:
            data['secret_question'] = secret_question

        if source_of_wealth:
            data['source_of_wealth'] = source_of_wealth

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
