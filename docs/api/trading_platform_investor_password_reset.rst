
Trading Platform: Investor Password Reset (trading_platform_investor_password_reset)
=====================================================================================================================

Reset the investor password of a Trading Platform Account

Auth Scope(s): :code:`admin`


.. py:method:: trading_platform_investor_password_reset(account_id: str, new_password: str, platform: str, verification_code: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param account_id: Trading account ID.
   :type account_id: str
   :param new_password: New password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
   :type new_password: str
   :param platform: Name of trading platform.
   :type platform: str
   :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
   :type verification_code: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.trading_platform_investor_password_reset

  binary.api.trading_platform_investor_password_reset(
      account_id='MTR1000'
      new_password='InvestPwd123@!'
      platform='mt5'
      verification_code='abCD0199'
  )

.. seealso::
   * `Binary API Docs for trading_platform_investor_password_reset <https://developers.binary.com/api/#trading_platform_investor_password_reset>`_
    