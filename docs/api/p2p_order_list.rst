
P2P Order List (p2p_order_list)
================================================================

List active orders.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_order_list(active: Optional[Union[int, float, Decimal]] = None, advert_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param active: [Optional] Should be 1 to list active, 0 to list inactive (historical).
   :type active: Optional[Union[int, float, Decimal]]
   :param advert_id: [Optional] If present, lists orders applying to a specific advert.
   :type advert_id: Optional[str]
   :param limit: [Optional] Used for paging.
   :type limit: Optional[int]
   :param offset: [Optional] Used for paging.
   :type offset: Optional[int]
   :param subscribe: [Optional] If set to 1, will send updates whenever there is a change to any order belonging to you.
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
  :name: binary.api.p2p_order_list

  binary.api.p2p_order_list(
      advert_id='1234'
  )

.. seealso::
   * `Binary API Docs for p2p_order_list <https://developers.binary.com/api/#p2p_order_list>`_
    