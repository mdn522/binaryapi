
Payment agent create (paymentagent_create)
===========================================================================

Saves client's payment agent details.

Auth Scope(s): :code:`admin`


.. py:method:: paymentagent_create(code_of_conduct_approval: int, commission_deposit: Union[int, float, Decimal], commission_withdrawal: Union[int, float, Decimal], email: str, information: str, payment_agent_name: str, supported_payment_methods: List, urls: List, affiliate_id: Optional[str] = None, phone_numbers: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param code_of_conduct_approval: Indicates client's agreement with the Code of Conduct.
   :type code_of_conduct_approval: int
   :param commission_deposit: Commission  (%) the agent wants to take on deposits
   :type commission_deposit: Union[int, float, Decimal]
   :param commission_withdrawal: Commission  (%) the agent wants to take on withdrawals
   :type commission_withdrawal: Union[int, float, Decimal]
   :param email: Payment agent's email address.
   :type email: str
   :param information: [Optional] Information about payment agent and their proposed service.
   :type information: str
   :param payment_agent_name: The name with which the payment agent is going to be identified.
   :type payment_agent_name: str
   :param supported_payment_methods: A list of supported payment methods.
   :type supported_payment_methods: List
   :param urls: The URL(s) of payment agent's website(s).
   :type urls: List
   :param affiliate_id: [Optional] Client's My Affiliate id, if exists.
   :type affiliate_id: Optional[str]
   :param phone_numbers: Payment agent's phone number(s) with country code.
   :type phone_numbers: Optional[List]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.paymentagent_create

  binary.api.paymentagent_create(
      affiliate_id='1231234'
      code_of_conduct_approval=1
      commission_deposit=2
      commission_withdrawal=3
      email='joe@joy.com'
      information='The best person you can find'
      payment_agent_name='Joe Joy'
      phone_numbers=[{'phone_number': '+923-22-23-13'}]
      supported_payment_methods=[{'payment_method': 'MasterCard'}, {'payment_method': 'Visa'}]
      urls=[{'url': 'https://abc.com'}]
  )

.. seealso::
   * `Binary API Docs for paymentagent_create <https://developers.binary.com/api/#paymentagent_create>`_
    