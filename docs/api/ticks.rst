
Ticks Stream (ticks)
=====================================================

Initiate a continuous stream of spot price updates for a given symbol.




.. py:method:: ticks(ticks: Union[List, str], subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param ticks: The short symbol name or array of symbols (obtained from `active_symbols` call).
   :type ticks: Union[List, str]
   :param subscribe: [Optional] If set to 1, will send updates whenever a new tick is received.
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
  :name: binary.api.ticks

  binary.api.ticks(
      'R_50'
      subscribe=1
  )

.. seealso::
   * `Binary API Docs for ticks <https://developers.binary.com/api/#ticks>`_
    