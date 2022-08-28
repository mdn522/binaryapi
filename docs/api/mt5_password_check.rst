
MT5: Password Check (mt5_password_check)
=========================================================================

This call validates the main password for the MT5 user

Auth Scope(s): :code:`admin`


.. py:method:: mt5_password_check(login: str, password: str, password_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param login: MT5 user login
   :type login: str
   :param password: The password of the account.
   :type password: str
   :param password_type: [Optional] Type of the password to check.
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
  :name: binary.api.mt5_password_check

  binary.api.mt5_password_check(
      login='MTR1000'
      password='abc1234'
      password_type='main'
  )

.. seealso::
   * `Binary API Docs for mt5_password_check <https://developers.binary.com/api/#mt5_password_check>`_
    