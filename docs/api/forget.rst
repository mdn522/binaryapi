
Forget (forget)
================================================

Immediately cancel the real-time stream of messages with a specific ID.




.. py:method:: forget(forget: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param forget: ID of the real-time stream of messages to cancel.
   :type forget: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.forget

  binary.api.forget(
      'd1ee7d0d-3ca9-fbb4-720b-5312d487185b'
  )

.. seealso::
   * `Binary API Docs for forget <https://developers.binary.com/api/#forget>`_
    