
Payment Agent: Withdraw (paymentagent_withdraw)
================================================================================

Initiate a withdrawal to an approved Payment Agent.

Auth Scope(s): :code:`payments`


.. py:method:: paymentagent_withdraw(amount: Union[int, float, Decimal], currency: str, paymentagent_loginid: str, verification_code: str, description: Optional[str] = None, dry_run: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param amount: The amount to withdraw to the payment agent.
   :type amount: Union[int, float, Decimal]
   :param currency: The currency code.
   :type currency: str
   :param paymentagent_loginid: The payment agent loginid received from the `paymentagent_list` call.
   :type paymentagent_loginid: str
   :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
   :type verification_code: str
   :param description: [Optional] Remarks about the withdraw. Only letters, numbers, space, period, comma, - ' are allowed.
   :type description: Optional[str]
   :param dry_run: [Optional] If set to 1, just do validation.
   :type dry_run: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.paymentagent_withdraw

  binary.api.paymentagent_withdraw(
      amount=1000
      currency='USD'
      paymentagent_loginid='CR100001'
      verification_code='my_verification_code'
  )

.. seealso::
   * `Binary API Docs for paymentagent_withdraw <https://developers.binary.com/api/#paymentagent_withdraw>`_
    