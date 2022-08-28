
Cashier Information (cashier)
==============================================================

Request the cashier info for the specified type.

Auth Scope(s): :code:`payments`


.. py:method:: cashier(cashier: str, address: Optional[str] = None, amount: Optional[Union[int, float, Decimal]] = None, dry_run: Optional[int] = None, provider: Optional[str] = None, type: Optional[str] = None, verification_code: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param cashier: Operation which needs to be requested from cashier
   :type cashier: str
   :param address: [Optional] Address for crypto withdrawal. Only applicable for `api` type.
   :type address: Optional[str]
   :param amount: [Optional] Amount for crypto withdrawal. Only applicable for `api` type.
   :type amount: Optional[Union[int, float, Decimal]]
   :param dry_run: [Optional] If set to `1`, only validation is performed. Only applicable for `withdraw` using `crypto` provider and `api` type.
   :type dry_run: Optional[int]
   :param provider: [Optional] Cashier provider. `crypto` will be default option for crypto currency accounts.
   :type provider: Optional[str]
   :param type: [Optional] Data need to be returned from cashier. `api` is supported only for `crypto` provider.
   :type type: Optional[str]
   :param verification_code: [Optional] Email verification code (received from a `verify_email` call, which must be done first)
   :type verification_code: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.cashier

  binary.api.cashier(
      'deposit'
      provider='doughflow'
      verification_code='my_verification_code'
  )

.. seealso::
   * `Binary API Docs for cashier <https://developers.binary.com/api/#cashier>`_
    