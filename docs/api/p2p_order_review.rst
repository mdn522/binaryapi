
P2P Order Review (p2p_order_review)
====================================================================

Creates a review for the specified order.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_order_review(order_id: str, rating: int, recommended: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param order_id: The order identification number.
   :type order_id: str
   :param rating: Rating for the transaction, 1 to 5.
   :type rating: int
   :param recommended: [Optional] `1` if the counterparty is recommendable to others, otherwise `0`.
   :type recommended: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_order_review

  binary.api.p2p_order_review(
      order_id='1234'
      rating=4
      recommended=1
  )

.. seealso::
   * `Binary API Docs for p2p_order_review <https://developers.binary.com/api/#p2p_order_review>`_
    