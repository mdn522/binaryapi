
P2P Chat Create (p2p_chat_create)
==================================================================

Creates a P2P chat for the specified order.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_chat_create(order_id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param order_id: The unique identifier for the order to create the chat for.
   :type order_id: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_chat_create

  binary.api.p2p_chat_create(
      order_id='1234'
  )

.. seealso::
   * `Binary API Docs for p2p_chat_create <https://developers.binary.com/api/#p2p_chat_create>`_
    