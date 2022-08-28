
Ping (ping)
============================================

To send the ping request to the server. Mostly used to test the connection or to keep it alive.




.. py:method:: ping(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.ping

  binary.api.ping()

.. seealso::
   * `Binary API Docs for ping <https://developers.binary.com/api/#ping>`_
    