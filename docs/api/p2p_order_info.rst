
P2P Order Information (p2p_order_info)
=======================================================================

Retrieves the information about a P2P order.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_order_info(id: str, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param id: The unique identifier for the order.
   :type id: str
   :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to order
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
  :name: binary.api.p2p_order_info

  binary.api.p2p_order_info(
      id='1234'
  )

.. seealso::
   * `Binary API Docs for p2p_order_info <https://developers.binary.com/api/#p2p_order_info>`_
    