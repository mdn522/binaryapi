
Copy Trading: Statistics (copytrading_statistics)
==================================================================================

Retrieve performance, trading, risk and copiers statistics of trader.




.. py:method:: copytrading_statistics(trader_id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param trader_id: The ID of the target trader.
   :type trader_id: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.copytrading_statistics

  binary.api.copytrading_statistics(
      trader_id='CR1234'
  )

.. seealso::
   * `Binary API Docs for copytrading_statistics <https://developers.binary.com/api/#copytrading_statistics>`_
    