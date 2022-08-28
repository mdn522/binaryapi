
P2P Advert List (p2p_advert_list)
==================================================================

Returns available adverts for use with `p2p_order_create` .

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advert_list(advertiser_id: Optional[str] = None, advertiser_name: Optional[str] = None, amount: Optional[Union[int, float, Decimal]] = None, counterparty_type: Optional[str] = None, favourites_only: Optional[int] = None, limit: Optional[int] = None, local_currency: Optional[str] = None, offset: Optional[int] = None, payment_method: Optional[List] = None, sort_by: Optional[str] = None, use_client_limits: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param advertiser_id: [Optional] ID of the advertiser to list adverts for.
   :type advertiser_id: Optional[str]
   :param advertiser_name: [Optional] Search for advertiser by name. Partial matches will be returned.
   :type advertiser_name: Optional[str]
   :param amount: [Optional] How much to buy or sell, used to calculate prices.
   :type amount: Optional[Union[int, float, Decimal]]
   :param counterparty_type: [Optional] Filter the adverts by `counterparty_type`.
   :type counterparty_type: Optional[str]
   :param favourites_only: [Optional] Only show adverts from favourite advertisers. Default is 0.
   :type favourites_only: Optional[int]
   :param limit: [Optional] Used for paging.
   :type limit: Optional[int]
   :param local_currency: [Optional] Currency to conduct payment transaction in, defaults to the main currency for the client's country.
   :type local_currency: Optional[str]
   :param offset: [Optional] Used for paging.
   :type offset: Optional[int]
   :param payment_method: [Optional] Search by supported payment methods.
   :type payment_method: Optional[List]
   :param sort_by: [Optional] How the results are sorted.
   :type sort_by: Optional[str]
   :param use_client_limits: [Optional] If set to 1, ads that exceed this account's balance or turnover limits will not be shown.
   :type use_client_limits: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advert_list

  binary.api.p2p_advert_list(
      counterparty_type='buy'
  )

.. seealso::
   * `Binary API Docs for p2p_advert_list <https://developers.binary.com/api/#p2p_advert_list>`_
    