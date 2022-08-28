
Forget All (forget_all)
========================================================

Immediately cancel the real-time streams of messages of given type.




.. py:method:: forget_all(forget_all: Union[List], passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param forget_all: Cancel all streams by type. The value can be either a single type e.g. `"ticks"`, or an array of multiple types e.g. `["candles", "ticks"]`.
   :type forget_all: Union[List]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.forget_all

  binary.api.forget_all(
      'ticks'
  )

.. seealso::
   * `Binary API Docs for forget_all <https://developers.binary.com/api/#forget_all>`_
    