
MT5: Deposit (mt5_deposit)
===========================================================

This call allows deposit into MT5 account from Binary account.

Auth Scope(s): :code:`payments`


.. py:method:: mt5_deposit(to_mt5: str, amount: Optional[Union[int, float, Decimal]] = None, from_binary: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param to_mt5: MT5 account login to deposit money to
   :type to_mt5: str
   :param amount: Amount to deposit (in the currency of from_binary); min = $1 or an equivalent amount, max = $20000 or an equivalent amount
   :type amount: Optional[Union[int, float, Decimal]]
   :param from_binary: Binary account loginid to transfer money from
   :type from_binary: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.mt5_deposit

  binary.api.mt5_deposit(
      amount=1000
      from_binary='CR100001'
      to_mt5='MTR1000'
  )

.. seealso::
   * `Binary API Docs for mt5_deposit <https://developers.binary.com/api/#mt5_deposit>`_
    