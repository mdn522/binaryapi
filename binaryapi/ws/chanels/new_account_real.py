"""Module for Binary new_account_real websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#new_account_real

class NewAccountReal(Base):
    """Class for Binary new_account_real websocket channel."""

    name = "new_account_real"

    def __call__(
        self, 
        account_opening_reason: Optional[str] = None, 
        account_turnover: Optional[str] = None, 
        address_city: Optional[str] = None, 
        address_line_1: Optional[str] = None, 
        address_line_2: Optional[str] = None, 
        address_postcode: Optional[str] = None, 
        address_state: Optional[str] = None, 
        affiliate_token: Optional[str] = None, 
        citizen: Optional[str] = None, 
        client_type: Optional[str] = None, 
        currency: Optional[str] = None, 
        date_of_birth: Optional[str] = None, 
        first_name: Optional[str] = None, 
        last_name: Optional[str] = None, 
        non_pep_declaration: Optional[int] = None, 
        phone: Optional[str] = None, 
        place_of_birth: Optional[str] = None, 
        residence: Optional[str] = None, 
        salutation: Optional[str] = None, 
        secret_answer: Optional[str] = None, 
        secret_question: Optional[str] = None, 
        tax_identification_number: Optional[str] = None, 
        tax_residence: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to new_account_real websocket channel.
        New Real-Money Account: Default Landing Company (request)
        This call opens a new real-money account. This call can be made from a virtual-money or a real-money account. If it is the latter, client information fields in this call will be ignored and data from your existing real-money account will be used.

        :param account_opening_reason: [Optional] Purpose and reason for requesting the account opening.
        :type account_opening_reason: Optional[str]
        :param account_turnover: [Optional] The anticipated account turnover.
        :type account_turnover: Optional[str]
        :param address_city: [Optional] Within 100 characters.
        :type address_city: Optional[str]
        :param address_line_1: Within 70 characters, with no leading whitespaces and may contain letters/numbers and/or any of following characters '.,:;()@#/-
        :type address_line_1: Optional[str]
        :param address_line_2: [Optional] Within 70 characters.
        :type address_line_2: Optional[str]
        :param address_postcode: [Optional] Within 20 characters and may not contain '+'.
        :type address_postcode: Optional[str]
        :param address_state: [Optional] Possible value receive from `states_list` call.
        :type address_state: Optional[str]
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: Optional[str]
        :param citizen: [Optional] Country of legal citizenship, 2-letter country code.
        :type citizen: Optional[str]
        :param client_type: [Optional] Indicates whether this is for a client requesting an account with professional status.
        :type client_type: Optional[str]
        :param currency: [Optional] To set currency of the account. List of supported currencies can be acquired with `payout_currencies` call.
        :type currency: Optional[str]
        :param date_of_birth: Date of birth format: `yyyy-mm-dd`.
        :type date_of_birth: Optional[str]
        :param first_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type first_name: Optional[str]
        :param last_name: Within 2-50 characters, use only letters, spaces, hyphens, full-stops or apostrophes.
        :type last_name: Optional[str]
        :param non_pep_declaration: [Optional] Indicates client's self-declaration of not being a PEP/RCA (Politically Exposed Person/Relatives and Close Associates).
        :type non_pep_declaration: Optional[int]
        :param phone: [Optional] Starting with `+` followed by 9-35 digits, hyphens or space.
        :type phone: Optional[str]
        :param place_of_birth: [Optional] Place of birth, 2-letter country code.
        :type place_of_birth: Optional[str]
        :param residence: 2-letter country code, possible value receive from `residence_list` call.
        :type residence: Optional[str]
        :param salutation: [Optional] Accept any value in enum list.
        :type salutation: Optional[str]
        :param secret_answer: [Optional] Answer to secret question, within 4-50 characters. Required for new account and existing client details will be used if client open another account.
        :type secret_answer: Optional[str]
        :param secret_question: [Optional] Accept any value in enum list. Required for new account and existing client details will be used if client open another account.
        :type secret_question: Optional[str]
        :param tax_identification_number: [Optional] Tax identification number. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_identification_number: Optional[str]
        :param tax_residence: [Optional] Residence for tax purpose. Comma separated iso country code if multiple jurisdictions. Only applicable for real money account. Required for `maltainvest` landing company.
        :type tax_residence: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "new_account_real": int(1)
        }

        if account_opening_reason:
            data['account_opening_reason'] = str(account_opening_reason)

        if account_turnover:
            data['account_turnover'] = str(account_turnover)

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

        if affiliate_token:
            data['affiliate_token'] = str(affiliate_token)

        if citizen:
            data['citizen'] = str(citizen)

        if client_type:
            data['client_type'] = str(client_type)

        if currency:
            data['currency'] = str(currency)

        if date_of_birth:
            data['date_of_birth'] = str(date_of_birth)

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
