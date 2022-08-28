
MT5: Password Reset (mt5_password_reset)
=========================================================================

To reset the password of MT5 account.

Auth Scope(s): :code:`admin`


.. py:method:: mt5_password_reset(login: str, new_password: str, verification_code: str, password_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param login: MT5 user login
   :type login: str
   :param new_password: New password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
   :type new_password: str
   :param verification_code: Email verification code (received from a `verify_email` call, which must be done first)
   :type verification_code: str
   :param password_type: [Optional] Type of the password to reset.
   :type password_type: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.mt5_password_reset

  binary.api.mt5_password_reset(
      login='MTD1000'
      new_password='C0rrect_p4ssword'
      password_type='main'
      verification_code='O8eZ2xMq'
  )

.. seealso::
   * `Binary API Docs for mt5_password_reset <https://developers.binary.com/api/#mt5_password_reset>`_
    