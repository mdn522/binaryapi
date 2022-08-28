
Balance (balance)
==================================================

Get user account balance

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: balance(account: Optional[str] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param account: [Optional] If set to `all`, return the balances of all accounts one by one; if set to `current`, return the balance of current account; if set as an account id, return the balance of that account.
   :type account: Optional[str]
   :param subscribe: [Optional] If set to 1, will send updates whenever the balance changes.
   :type subscribe: Optional[Union[bool, int]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.balance

  binary.api.balance(
      subscribe=1
  )

.. seealso::
   * `Binary API Docs for balance <https://developers.binary.com/api/#balance>`_
    