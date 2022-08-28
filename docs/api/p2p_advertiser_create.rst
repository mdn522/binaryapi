
P2P Advertiser Create (p2p_advertiser_create)
==============================================================================

Registers the client as a P2P advertiser.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_create(name: str, contact_info: Optional[str] = None, default_advert_description: Optional[str] = None, payment_info: Optional[str] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param name: The advertiser's displayed name.
   :type name: str
   :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
   :type contact_info: Optional[str]
   :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
   :type default_advert_description: Optional[str]
   :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
   :type payment_info: Optional[str]
   :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to advertiser
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
  :name: binary.api.p2p_advertiser_create

  binary.api.p2p_advertiser_create(
      name='your_name'
  )

.. seealso::
   * `Binary API Docs for p2p_advertiser_create <https://developers.binary.com/api/#p2p_advertiser_create>`_
    