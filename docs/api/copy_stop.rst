
Copy Trading: Stop (copy_stop)
===============================================================

Stop copy trader bets

Auth Scope(s): :code:`trade`


.. py:method:: copy_stop(copy_stop: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param copy_stop: API tokens identifying the accounts which needs not to be copied
   :type copy_stop: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.copy_stop

  binary.api.copy_stop(
      'uw2mk7no3oktoRVVsB4Dz7TQnFgrthg'
  )

.. seealso::
   * `Binary API Docs for copy_stop <https://developers.binary.com/api/#copy_stop>`_
    