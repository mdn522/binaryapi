
P2P Advertiser Update (p2p_advertiser_update)
==============================================================================

Update the information of the P2P advertiser for the current account. Can only be used by an approved P2P advertiser.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_update(contact_info: Optional[str] = None, default_advert_description: Optional[str] = None, is_listed: Optional[int] = None, payment_info: Optional[str] = None, show_name: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
   :type contact_info: Optional[str]
   :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
   :type default_advert_description: Optional[str]
   :param is_listed: [Optional] Used to set if the advertiser's adverts could be listed. When `0`, adverts won't be listed regardless of they are active or not. This doesn't change the `is_active` of each individual advert.
   :type is_listed: Optional[int]
   :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
   :type payment_info: Optional[str]
   :param show_name: [Optional] When `1`, the advertiser's real name will be displayed on to other users on adverts and orders.
   :type show_name: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advertiser_update

  binary.api.p2p_advertiser_update(
      is_listed=0
  )

.. seealso::
   * `Binary API Docs for p2p_advertiser_update <https://developers.binary.com/api/#p2p_advertiser_update>`_
    