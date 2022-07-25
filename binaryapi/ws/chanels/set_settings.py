"""Module for Binary set_settings websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#set_settings

class SetSettings(Base):
    """Class for Binary set_settings websocket channel."""

    name = "set_settings"

    def __call__(
        self, 
        account_opening_reason: Optional[str] = None, 
        address_city: Optional[str] = None, 
        address_line_1: Optional[str] = None, 
        address_line_2: Optional[str] = None, 
        address_postcode: Optional[str] = None, 
        address_state: Optional[str] = None, 
        allow_copiers: Optional[int] = None, 
        citizen: Optional[str] = None, 
        date_of_birth: Optional[str] = None, 
        email_consent: Optional[int] = None, 
        feature_flag=None, 
        first_name: Optional[str] = None, 
        last_name: Optional[str] = None, 
        non_pep_declaration: Optional[int] = None, 
        phone: Optional[str] = None, 
        place_of_birth: Optional[str] = None, 
        preferred_language: Optional[str] = None, 
        request_professional_status: Optional[int] = None, 
        residence: Optional[str] = None, 
        salutation: Optional[str] = None, 
        secret_answer: Optional[str] = None, 
        secret_question: Optional[str] = None, 
        tax_identification_number: Optional[str] = None, 
        tax_residence: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to set_settings websocket channel.
        Set Account Settings (request)
        Set User Settings (this call should be used in conjunction with `get_settings`)

        :param account_opening_reason: [Optional] Purpose and reason for requesting the account opening. Only applicable for real money account. Required for clients that have not set it yet. Can only be set once.
        :type account_opening_reason: Optional[str]
        :param address_city: [Optional] Note: not applicable for virtual account. Required field for real money account.
        :type address_city: Optional[str]
        :param address_line_1: [Optional] Note: not applicable for virtual account. Required field for real money account.
        :type address_line_1: Optional[str]
        :param address_line_2: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_line_2: Optional[str]
        :param address_postcode: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_postcode: Optional[str]
        :param address_state: [Optional] Note: not applicable for virtual account. Optional field for real money account.
        :type address_state: Optional[str]
        :param allow_copiers: [Optional] Boolean value 1 or 0, indicating permission to allow others to follow your trades. Note: not applicable for Virtual account. Only allow for real money account.
        :type allow_copiers: Optional[int]
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code.
        :type citizen: Optional[str]
        :param date_of_birth: [Optional] Date of birth format: yyyy-mm-dd (can only be changed on unauthenticated svg accounts).
        :type date_of_birth: Optional[str]
        :param email_consent: [Optional] Boolean value 1 or 0, indicating permission to use email address for any contact which may include marketing
        :type email_consent: Optional[int]
        :param feature_flag: [Optional] Enable or disable one or multiple features.
        :type feature_flag: 
        :param first_name: [Optional] Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes (can only be changed on unauthenticated svg accounts).
        :type first_name: Optional[str]
        :param last_name: [Optional] Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes (can only be changed on unauthenticated svg accounts).
        :type last_name: Optional[str]
        :param non_pep_declaration: [Optional] Indicates client's self-declaration of not being a PEP/RCA (Politically Exposed Person/Relatives and Close Associates). Effective for real accounts only.
        :type non_pep_declaration: Optional[int]
        :param phone: [Optional] Note: not applicable for virtual account. Starting with `+` followed by 9-35 digits, hyphens or space.
        :type phone: Optional[str]
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: Optional[str]
        :param preferred_language: [Optional] User's preferred language, ISO standard language code
        :type preferred_language: Optional[str]
        :param request_professional_status: [Optional] Required when client wants to be treated as professional. Applicable for financial accounts only.
        :type request_professional_status: Optional[int]
        :param residence: [Optional] 2-letter country code. Note: not applicable for real money account. Only allow for Virtual account without residence set.
        :type residence: Optional[str]
        :param salutation: [Optional] Accept any value in enum list (can only be changed on unauthenticated svg accounts).
        :type salutation: Optional[str]
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters. Required for new account and existing client details will be used if client opens another account.
        :type secret_answer: Optional[str]
        :param secret_question: [Optional] Accept any value in enum list. Required for new account and existing client details will be used if client opens another account.
        :type secret_question: Optional[str]
        :param tax_identification_number: [Optional] Tax identification number. Only applicable for real money account. Required for maltainvest landing company.
        :type tax_identification_number: Optional[str]
        :param tax_residence: [Optional] Residence for tax purpose. Comma separated iso country code if multiple jurisdictions. Only applicable for real money account. Required for maltainvest landing company.
        :type tax_residence: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "set_settings": int(1)
        }

        if account_opening_reason:
            data['account_opening_reason'] = str(account_opening_reason)

        if address_city:
            data['address_city'] = str(address_city)

        if address_line_1:
            data['address_line_1'] = str(address_line_1)

        if address_line_2:
            data['address_line_2'] = str(address_line_2)

        if address_postcode:
            data['address_postcode'] = str(address_postcode)

        if address_state:
            data['address_state'] = str(address_state)

        if allow_copiers:
            data['allow_copiers'] = int(allow_copiers)

        if citizen:
            data['citizen'] = str(citizen)

        if date_of_birth:
            data['date_of_birth'] = str(date_of_birth)

        if email_consent:
            data['email_consent'] = int(email_consent)

        if feature_flag:
            data['feature_flag'] = feature_flag

        if first_name:
            data['first_name'] = str(first_name)

        if last_name:
            data['last_name'] = str(last_name)

        if non_pep_declaration:
            data['non_pep_declaration'] = int(non_pep_declaration)

        if phone:
            data['phone'] = str(phone)

        if place_of_birth:
            data['place_of_birth'] = str(place_of_birth)

        if preferred_language:
            data['preferred_language'] = str(preferred_language)

        if request_professional_status:
            data['request_professional_status'] = int(request_professional_status)

        if residence:
            data['residence'] = str(residence)

        if salutation:
            data['salutation'] = str(salutation)

        if secret_answer:
            data['secret_answer'] = str(secret_answer)

        if secret_question:
            data['secret_question'] = str(secret_question)

        if tax_identification_number:
            data['tax_identification_number'] = str(tax_identification_number)

        if tax_residence:
            data['tax_residence'] = str(tax_residence)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
