
MT5: Withdrawal (mt5_withdrawal)
=================================================================

This call allows withdrawal from MT5 account to Binary account.

Auth Scope(s): :code:`payments`


.. py:method:: mt5_withdrawal(amount: Union[int, float, Decimal], from_mt5: str, to_binary: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param amount: Amount to withdraw (in the currency of the MT5 account); min = $1 or an equivalent amount, max = $20000 or an equivalent amount.
   :type amount: Union[int, float, Decimal]
   :param from_mt5: MT5 account login to withdraw money from
   :type from_mt5: str
   :param to_binary: Binary account loginid to transfer money to
   :type to_binary: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.mt5_withdrawal

  binary.api.mt5_withdrawal(
      amount=1000
      from_mt5='MTR1000'
      to_binary='CR100001'
  )

.. seealso::
   * `Binary API Docs for mt5_withdrawal <https://developers.binary.com/api/#mt5_withdrawal>`_
    