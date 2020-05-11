"""Module for Binary set_settings websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#set_settings

class SetSettings(Base):
    """Class for Binary set_settings websocket chanel."""

    name = "set_settings"

    def __call__(self, account_opening_reason: str=None, address_city: str=None, address_line_1: str=None, address_line_2=None, address_postcode: str=None, address_state: str=None, allow_copiers: int=None, citizen=None, date_of_birth: str=None, email_consent: int=None, first_name: str=None, last_name: str=None, phone: str=None, place_of_birth: str=None, request_professional_status: int=None, residence=None, salutation: str=None, secret_answer: str=None, secret_question: str=None, tax_identification_number: str=None, tax_residence: str=None, passthrough=None, req_id: int=None):
        """Method to send message to set_settings websocket chanel.
        Set Account Settings (request)
        Set User Settings (this call should be used in conjunction with `get_settings`)
        :param account_opening_reason: [Optional] Purpose and reason for requesting the account opening. Only applicable for real money account. Required for clients that have not set it yet. Can only be set once.
        :type account_opening_reason: str
        :param address_city: [Optional] Note: not applicable for virtual account. Required field for real money account.
        :type address_city: str
        :param address_line_1: [Optional] Note: not applicable for virtual account. Required field for real money account.
        :type address_line_1: str
        :param address_line_2: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_line_2: 
        :param address_postcode: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_postcode: str
        :param address_state: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_state: str
        :param allow_copiers: [Optional] Boolean value 1 or 0, indicating permission to allow others to follow your trades. Note: not applicable for Virtual account. Only allow for real money account.
        :type allow_copiers: int
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code.
        :type citizen: 
        :param date_of_birth: [Optional] Date of birth format: yyyy-mm-dd (can only be changed on unauthenticated svg accounts).
        :type date_of_birth: str
        :param email_consent: [Optional] Boolean value 1 or 0, indicating permission to use email address for any contact which may include marketing
        :type email_consent: int
        :param first_name: [Optional] Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes (can only be changed on unauthenticated svg accounts).
        :type first_name: str
        :param last_name: [Optional] Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes (can only be changed on unauthenticated svg accounts).
        :type last_name: str
        :param phone: [Optional] Note: not applicable for virtual account. Required field for real money account. Starting with `+` followed by 8-35 digits, allowing hyphens or space.
        :type phone: str
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: str
        :param request_professional_status: [Optional] Required when client wants to be treated as professional. Applicable for financial accounts only.
        :type request_professional_status: int
        :param residence: [Optional] 2-letter country code. Note: not applicable for real money account. Only allow for Virtual account without residence set.
        :type residence: 
        :param salutation: [Optional] Accept any value in enum list (can only be changed on unauthenticated svg accounts).
        :type salutation: str
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters. Required for new account and existing client details will be used if client opens another account.
        :type secret_answer: str
        :param secret_question: [Optional] Accept any value in enum list. Required for new account and existing client details will be used if client opens another account.
        :type secret_question: str
        :param tax_identification_number: [Optional] Tax identification number. Only applicable for real money account. Required for maltainvest landing company.
        :type tax_identification_number: str
        :param tax_residence: [Optional] Residence for tax purpose. Comma separated iso country code if multiple jurisdictions. Only applicable for real money account. Required for maltainvest landing company.
        :type tax_residence: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "set_settings": 1
        }

        if account_opening_reason:
            data['account_opening_reason'] = account_opening_reason

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

        if allow_copiers:
            data['allow_copiers'] = allow_copiers

        if citizen:
            data['citizen'] = citizen

        if date_of_birth:
            data['date_of_birth'] = date_of_birth

        if email_consent:
            data['email_consent'] = email_consent

        if first_name:
            data['first_name'] = first_name

        if last_name:
            data['last_name'] = last_name

        if phone:
            data['phone'] = phone

        if place_of_birth:
            data['place_of_birth'] = place_of_birth

        if request_professional_status:
            data['request_professional_status'] = request_professional_status

        if residence:
            data['residence'] = residence

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
