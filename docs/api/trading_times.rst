
Trading Times (trading_times)
==============================================================

Receive a list of market opening times for a given date.




.. py:method:: trading_times(trading_times: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param trading_times: Date to receive market opening times for. (`yyyy-mm-dd` format. `today` can also be specified).
   :type trading_times: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.trading_times

  binary.api.trading_times(
      '2015-09-14'
  )

.. seealso::
   * `Binary API Docs for trading_times <https://developers.binary.com/api/#trading_times>`_
    