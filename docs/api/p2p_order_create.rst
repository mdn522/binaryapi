
P2P Order Create (p2p_order_create)
====================================================================

Creates a P2P order for the specified advert.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_order_create(advert_id: str, amount: Union[int, float, Decimal], contact_info: Optional[str] = None, payment_info: Optional[str] = None, payment_method_ids: Optional[List] = None, rate: Optional[Union[int, float, Decimal]] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param advert_id: The unique identifier for the advert to create an order against.
   :type advert_id: str
   :param amount: The amount of currency to be bought or sold.
   :type amount: Union[int, float, Decimal]
   :param contact_info: [Optional] Seller contact information. Only applicable for 'sell orders'.
   :type contact_info: Optional[str]
   :param payment_info: [Optional] Payment instructions, only applicable for sell orders.
   :type payment_info: Optional[str]
   :param payment_method_ids: IDs of payment methods, only applicable for sell orders.
   :type payment_method_ids: Optional[List]
   :param rate: [Optional] Conversion rate from account currency to local currency, only applicable for floating rate adverts.
   :type rate: Optional[Union[int, float, Decimal]]
   :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to the order.
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
  :name: binary.api.p2p_order_create

  binary.api.p2p_order_create(
      advert_id='1234'
      amount=100
  )

.. seealso::
   * `Binary API Docs for p2p_order_create <https://developers.binary.com/api/#p2p_order_create>`_
    