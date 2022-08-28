
Set Account Settings (set_settings)
====================================================================

Set User Settings (this call should be used in conjunction with `get_settings`)

Auth Scope(s): :code:`admin`


.. py:method:: set_settings(account_opening_reason: Optional[str] = None, address_city: Optional[str] = None, address_line_1: Optional[str] = None, address_line_2: Optional[str] = None, address_postcode: Optional[str] = None, address_state: Optional[str] = None, allow_copiers: Optional[int] = None, citizen: Optional[str] = None, date_of_birth: Optional[str] = None, email_consent: Optional[int] = None, feature_flag=None, first_name: Optional[str] = None, last_name: Optional[str] = None, non_pep_declaration: Optional[int] = None, phone: Optional[str] = None, place_of_birth: Optional[str] = None, preferred_language: Optional[str] = None, request_professional_status: Optional[int] = None, residence: Optional[str] = None, salutation: Optional[str] = None, secret_answer: Optional[str] = None, secret_question: Optional[str] = None, tax_identification_number: Optional[str] = None, tax_residence: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

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


Example
"""""""

.. code-block:: python
  :name: binary.api.set_settings

  binary.api.set_settings(
      account_opening_reason='Speculative'
      address_city='Test City'
      address_line_1='Test Address Line 1'
      address_line_2='Test Address Line 2'
      address_postcode='123456'
      allow_copiers=1
      email_consent=0
      phone='+15417543010'
      place_of_birth='ar'
      preferred_language='EN'
      request_professional_status=1
      tax_identification_number='987654321'
      tax_residence='hk'
  )

.. seealso::
   * `Binary API Docs for set_settings <https://developers.binary.com/api/#set_settings>`_
    