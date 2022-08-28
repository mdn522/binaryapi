
P2P Order Confirm (p2p_order_confirm)
======================================================================

Confirm a P2P order.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_order_confirm(id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param id: The unique identifier for this order.
   :type id: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_order_confirm

  binary.api.p2p_order_confirm(
      id='1234'
  )

.. seealso::
   * `Binary API Docs for p2p_order_confirm <https://developers.binary.com/api/#p2p_order_confirm>`_
    