
Server Time (time)
===================================================

Request back-end server epoch time.




.. py:method:: time(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.time

  binary.api.time()

.. seealso::
   * `Binary API Docs for time <https://developers.binary.com/api/#time>`_
    