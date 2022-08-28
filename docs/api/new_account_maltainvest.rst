
New Real-Money Account: Deriv Investment (Europe) Ltd (new_account_maltainvest)
================================================================================================================

This call opens a new real-money account with the `maltainvest` Landing Company. This call can be made from a virtual-money account or real-money account at Deriv (Europe) Limited. If it is the latter, client information fields in this call will be ignored and data from your existing real-money account will be used.

Auth Scope(s): :code:`admin`


.. py:method:: new_account_maltainvest(accept_risk: int, address_city: str, address_line_1: str, date_of_birth: str, education_level: str, employment_industry: str, estimated_worth: str, first_name: str, income_source: str, last_name: str, net_income: str, occupation: str, residence: str, salutation: str, tax_identification_number: str, tax_residence: str, account_opening_reason: Optional[str] = None, account_turnover: Optional[str] = None, address_line_2: Optional[str] = None, address_postcode: Optional[str] = None, address_state: Optional[str] = None, affiliate_token: Optional[str] = None, binary_options_trading_experience: Optional[str] = None, binary_options_trading_frequency: Optional[str] = None, cfd_trading_experience: Optional[str] = None, cfd_trading_frequency: Optional[str] = None, citizen: Optional[str] = None, client_type: Optional[str] = None, currency: Optional[str] = None, employment_status: Optional[str] = None, forex_trading_experience: Optional[str] = None, forex_trading_frequency: Optional[str] = None, non_pep_declaration: Optional[int] = None, other_instruments_trading_experience: Optional[str] = None, other_instruments_trading_frequency: Optional[str] = None, phone: Optional[str] = None, place_of_birth: Optional[str] = None, secret_answer: Optional[str] = None, secret_question: Optional[str] = None, source_of_wealth: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

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


Example
"""""""

.. code-block:: python
  :name: binary.api.new_account_maltainvest

  binary.api.new_account_maltainvest(
      accept_risk=1
      account_opening_reason='Speculative'
      account_turnover='Less than $25,000'
      address_city='Melbourne'
      address_line_1='20 Broadway Av'
      address_line_2='East Melbourne VIC'
      address_postcode='3002'
      address_state='Victoria'
      binary_options_trading_experience='1-2 years'
      binary_options_trading_frequency='40 transactions or more in the past 12 months'
      cfd_trading_experience='1-2 years'
      cfd_trading_frequency='0-5 transactions in the past 12 months'
      citizen='de'
      date_of_birth='1980-01-31'
      education_level='Secondary'
      employment_industry='Finance'
      employment_status='Self-Employed'
      estimated_worth='$100,000 - $250,000'
      first_name='Peter'
      forex_trading_experience='Over 3 years'
      forex_trading_frequency='0-5 transactions in the past 12 months'
      income_source='Self-Employed'
      last_name='Pan'
      net_income='$25,000 - $50,000'
      non_pep_declaration=1
      occupation='Managers'
      other_instruments_trading_experience='Over 3 years'
      other_instruments_trading_frequency='6-10 transactions in the past 12 months'
      phone='+6123456789'
      place_of_birth='nl'
      residence='de'
      salutation='Mr'
      secret_answer='Jones'
      secret_question="Mother's maiden name"
      source_of_wealth='Company Ownership'
      tax_identification_number='111-222-333'
      tax_residence='de,nl'
  )

.. seealso::
   * `Binary API Docs for new_account_maltainvest <https://developers.binary.com/api/#new_account_maltainvest>`_
    