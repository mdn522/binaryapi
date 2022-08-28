
Set Financial Assessment (set_financial_assessment)
====================================================================================

This call sets the financial assessment details based on the client's answers to analyze whether they possess the experience and knowledge to understand the risks involved with binary options trading.

Auth Scope(s): :code:`admin`


.. py:method:: set_financial_assessment(education_level: str, employment_industry: str, estimated_worth: str, income_source: str, net_income: str, occupation: str, account_turnover: Optional[str] = None, binary_options_trading_experience: Optional[str] = None, binary_options_trading_frequency: Optional[str] = None, cfd_trading_experience: Optional[str] = None, cfd_trading_frequency: Optional[str] = None, employment_status: Optional[str] = None, forex_trading_experience: Optional[str] = None, forex_trading_frequency: Optional[str] = None, other_instruments_trading_experience: Optional[str] = None, other_instruments_trading_frequency: Optional[str] = None, source_of_wealth: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param education_level: Level of Education.
   :type education_level: str
   :param employment_industry: Industry of Employment.
   :type employment_industry: str
   :param estimated_worth: Estimated Net Worth.
   :type estimated_worth: str
   :param income_source: Income Source.
   :type income_source: str
   :param net_income: Net Annual Income.
   :type net_income: str
   :param occupation: Occupation.
   :type occupation: str
   :param account_turnover: [Optional] The anticipated account turnover.
   :type account_turnover: Optional[str]
   :param binary_options_trading_experience: [Optional] Binary options trading experience.
   :type binary_options_trading_experience: Optional[str]
   :param binary_options_trading_frequency: [Optional] Binary options trading frequency.
   :type binary_options_trading_frequency: Optional[str]
   :param cfd_trading_experience: [Optional] CFDs trading experience.
   :type cfd_trading_experience: Optional[str]
   :param cfd_trading_frequency: [Optional] CFDs trading frequency.
   :type cfd_trading_frequency: Optional[str]
   :param employment_status: [Optional] Employment Status.
   :type employment_status: Optional[str]
   :param forex_trading_experience: [Optional] Forex trading experience.
   :type forex_trading_experience: Optional[str]
   :param forex_trading_frequency: [Optional] Forex trading frequency.
   :type forex_trading_frequency: Optional[str]
   :param other_instruments_trading_experience: [Optional] Trading experience in other financial instruments.
   :type other_instruments_trading_experience: Optional[str]
   :param other_instruments_trading_frequency: [Optional] Trading frequency in other financial instruments.
   :type other_instruments_trading_frequency: Optional[str]
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
  :name: binary.api.set_financial_assessment

  binary.api.set_financial_assessment(
      account_turnover='Less than $25,000'
      binary_options_trading_experience='1-2 years'
      binary_options_trading_frequency='40 transactions or more in the past 12 months'
      cfd_trading_experience='Over 3 years'
      cfd_trading_frequency='6-10 transactions in the past 12 months'
      education_level='Secondary'
      employment_industry='Finance'
      employment_status='Self-Employed'
      estimated_worth='$100,000 - $250,000'
      forex_trading_experience='Over 3 years'
      forex_trading_frequency='0-5 transactions in the past 12 months'
      income_source='Self-Employed'
      net_income='$25,000 - $50,000'
      occupation='Managers'
      other_instruments_trading_experience='Over 3 years'
      other_instruments_trading_frequency='6-10 transactions in the past 12 months'
      source_of_wealth='Company Ownership'
  )

.. seealso::
   * `Binary API Docs for set_financial_assessment <https://developers.binary.com/api/#set_financial_assessment>`_
    