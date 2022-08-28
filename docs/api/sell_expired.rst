
Sell Expired Contracts (sell_expired)
======================================================================

This call will try to sell any expired contracts and return the number of sold contracts.

Auth Scope(s): :code:`trade`


.. py:method:: sell_expired(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.sell_expired

  binary.api.sell_expired()

.. seealso::
   * `Binary API Docs for sell_expired <https://developers.binary.com/api/#sell_expired>`_
    