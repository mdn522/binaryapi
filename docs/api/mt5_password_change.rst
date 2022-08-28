
MT5: Password Change (mt5_password_change)
===========================================================================

To change passwords of the MT5 account.

Auth Scope(s): :code:`admin`


.. py:method:: mt5_password_change(login: str, new_password: str, old_password: str, password_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param login: MT5 user login
   :type login: str
   :param new_password: New password of the account. For validation (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
   :type new_password: str
   :param old_password: Old password for validation (non-empty string, accepts any printable ASCII character)
   :type old_password: str
   :param password_type: [Optional] Type of the password to change.
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
  :name: binary.api.mt5_password_change

  binary.api.mt5_password_change(
      login='MTR1000'
      new_password='C0rrect_p4ssword'
      old_password='Abc1234'
      password_type='main'
  )

.. seealso::
   * `Binary API Docs for mt5_password_change <https://developers.binary.com/api/#mt5_password_change>`_
    