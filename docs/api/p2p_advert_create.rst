
P2P Advert Create (p2p_advert_create)
======================================================================

Creates a P2P (Peer to Peer) advert. Can only be used by an approved P2P advertiser.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advert_create(amount: Union[int, float, Decimal], max_order_amount: Union[int, float, Decimal], min_order_amount: Union[int, float, Decimal], rate: Union[int, float, Decimal], type: str, contact_info: Optional[str] = None, description: Optional[str] = None, local_currency: Optional[str] = None, payment_info: Optional[str] = None, payment_method: Optional[str] = None, payment_method_ids: Optional[List] = None, payment_method_names: Optional[List] = None, rate_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param amount: The total amount of the advert, in advertiser's account currency.
   :type amount: Union[int, float, Decimal]
   :param max_order_amount: Maximum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be more than or equal to `min_order_amount`
   :type max_order_amount: Union[int, float, Decimal]
   :param min_order_amount: Minimum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be less than or equal to `max_order_amount`.
   :type min_order_amount: Union[int, float, Decimal]
   :param rate: Conversion rate from advertiser's account currency to `local_currency`. An absolute rate value (fixed), or percentage offset from current market rate (floating).
   :type rate: Union[int, float, Decimal]
   :param type: The advertisement represents the intention to perform this action on your Deriv account funds.
   :type type: str
   :param contact_info: [Optional] Advertiser contact information.
   :type contact_info: Optional[str]
   :param description: [Optional] General information about the advert.
   :type description: Optional[str]
   :param local_currency: [Optional] Local currency for this advert. If not provided, will use the currency of client's residence by default.
   :type local_currency: Optional[str]
   :param payment_info: [Optional] Payment instructions.
   :type payment_info: Optional[str]
   :param payment_method: [Optional] Payment method name (deprecated).
   :type payment_method: Optional[str]
   :param payment_method_ids: IDs of previously saved payment methods as returned from p2p_advertiser_payment_methods, only applicable for sell ads.
   :type payment_method_ids: Optional[List]
   :param payment_method_names: Payment method identifiers as returned from p2p_payment_methods, only applicable for buy ads.
   :type payment_method_names: Optional[List]
   :param rate_type: Type of rate, fixed or floating.
   :type rate_type: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advert_create

  binary.api.p2p_advert_create(
      description='Please transfer to account number 1234'
      type='buy'
      amount=100
      max_order_amount=50
      min_order_amount=20
      payment_method='bank_transfer'
      rate=4.25
  )

.. seealso::
   * `Binary API Docs for p2p_advert_create <https://developers.binary.com/api/#p2p_advert_create>`_
    