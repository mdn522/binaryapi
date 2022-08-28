
Copy Trading: Start (copy_start)
=================================================================

Start copy trader bets

Auth Scope(s): :code:`trade`


.. py:method:: copy_start(copy_start: str, assets: Optional[Union[List, str]] = None, max_trade_stake: Optional[Union[int, float, Decimal]] = None, min_trade_stake: Optional[Union[int, float, Decimal]] = None, trade_types: Optional[Union[List, str]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param copy_start: API tokens identifying the accounts of trader which will be used to copy trades
   :type copy_start: str
   :param assets: [Optional] Used to set assets to be copied. E.x ["frxUSDJPY", "R_50"]
   :type assets: Optional[Union[List, str]]
   :param max_trade_stake: [Optional] Used to set maximum trade stake to be copied.
   :type max_trade_stake: Optional[Union[int, float, Decimal]]
   :param min_trade_stake: [Optional] Used to set minimal trade stake to be copied.
   :type min_trade_stake: Optional[Union[int, float, Decimal]]
   :param trade_types: [Optional] Used to set trade types to be copied. E.x ["CALL", "PUT"]
   :type trade_types: Optional[Union[List, str]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.copy_start

  binary.api.copy_start(
      'uw2mk7no3oktoRVVsB4Dz7TQnFgrthg'
  )

.. seealso::
   * `Binary API Docs for copy_start <https://developers.binary.com/api/#copy_start>`_
    