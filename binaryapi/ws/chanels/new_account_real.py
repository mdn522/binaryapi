"""Module for Binary new_account_real websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#new_account_real

class NewAccountReal(Base):
    """Class for Binary new_account_real websocket chanel."""

    name = "new_account_real"

    def __call__(self, date_of_birth: str, first_name: str, last_name: str, residence: str, account_opening_reason: str=None, account_turnover: str=None, address_city: str=None, address_line_1: str=None, address_line_2: str=None, address_postcode: str=None, address_state: str=None, affiliate_token: str=None, citizen=None, client_type: str=None, currency: str=None, non_pep_declaration: int=None, phone: str=None, place_of_birth: str=None, salutation: str=None, secret_answer: str=None, secret_question: str=None, tax_identification_number: str=None, tax_residence: str=None, passthrough=None, req_id: int=None):
        """Method to send message to new_account_real websocket chanel.
        New Real-Money Account: Default Landing Company (request)
        This call opens a new real-money account. This call can be made from a virtual-money or a real-money account. If it is the latter, client information fields in this call will be ignored and data from your existing real-money account will be used.
        :param date_of_birth: Date of birth format: `yyyy-mm-dd`.
        :type date_of_birth: str
        :param first_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type first_name: str
        :param last_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type last_name: str
        :param residence: 2-letter country code, possible value receive from `residence_list` call.
        :type residence: str
        :param account_opening_reason: [Optional] Purpose and reason for requesting the account opening.
        :type account_opening_reason: str
        :param account_turnover: [Optional] The anticipated account turnover.
        :type account_turnover: str
        :param address_city: [Optional] Within 35 characters.
        :type address_city: str
        :param address_line_1: [Optional] Mailing address.
        :type address_line_1: str
        :param address_line_2: [Optional] Within 70 characters.
        :type address_line_2: str
        :param address_postcode: [Optional] Within 20 characters and may not contain '+'.
        :type address_postcode: str
        :param address_state: [Optional] Possible value receive from `states_list` call.
        :type address_state: str
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: str
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code.
        :type citizen: 
        :param client_type: [Optional] Indicates whether this is for a client requesting an account with professional status.
        :type client_type: str
        :param currency: [Optional] To set currency of the account. List of supported currencies can be acquired with `payout_currencies` call.
        :type currency: str
        :param non_pep_declaration: [Optional] Indicates client's self-declaration of not being a PEP/RCA.
        :type non_pep_declaration: int
        :param phone: [Optional] Starting with `+` followed by 8-35 digits, allowing hyphens or space.
        :type phone: str
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: str
        :param salutation: [Optional] Accept any value in enum list.
        :type salutation: str
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters. Required for new account and existing client details will be used if client open another account.
        :type secret_answer: str
        :param secret_question: [Optional] Accept any value in enum list. Required for new account and existing client details will be used if client open another account.
        :type secret_question: str
        :param tax_identification_number: [Optional] Tax identification number. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_identification_number: str
        :param tax_residence: [Optional] Residence for tax purpose. Comma separated iso country code if multiple jurisdictions. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_residence: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "new_account_real": 1,
            "date_of_birth": date_of_birth,
            "first_name": first_name,
            "last_name": last_name,
            "residence": residence
        }

        if account_opening_reason:
            data['account_opening_reason'] = account_opening_reason

        if account_turnover:
            data['account_turnover'] = account_turnover

        if address_city:
            data['address_city'] = address_city

        if address_line_1:
            data['address_line_1'] = address_line_1

        if address_line_2:
            data['address_line_2'] = address_line_2

        if address_postcode:
            data['address_postcode'] = address_postcode

        if address_state:
            data['address_state'] = address_state

        if affiliate_token:
            data['affiliate_token'] = affiliate_token

        if citizen:
            data['citizen'] = citizen

        if client_type:
            data['client_type'] = client_type

        if currency:
            data['currency'] = currency

        if non_pep_declaration:
            data['non_pep_declaration'] = non_pep_declaration

        if phone:
            data['phone'] = phone

        if place_of_birth:
            data['place_of_birth'] = place_of_birth

        if salutation:
            data['salutation'] = salutation

        if secret_answer:
            data['secret_answer'] = secret_answer

        if secret_question:
            data['secret_question'] = secret_question

        if tax_identification_number:
            data['tax_identification_number'] = tax_identification_number

        if tax_residence:
            data['tax_residence'] = tax_residence

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
