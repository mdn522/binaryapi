
P2P Advertiser Relations (p2p_advertiser_relations)
====================================================================================

Updates and returns favourite and blocked advertisers of the current user.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_relations(add_blocked: Optional[List] = None, add_favourites: Optional[List] = None, remove_blocked: Optional[List] = None, remove_favourites: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param add_blocked: IDs of advertisers to block.
   :type add_blocked: Optional[List]
   :param add_favourites: IDs of advertisers to add as favourites.
   :type add_favourites: Optional[List]
   :param remove_blocked: IDs of advertisers to remove from blocked.
   :type remove_blocked: Optional[List]
   :param remove_favourites: IDs of advertisers to remove from favourites.
   :type remove_favourites: Optional[List]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advertiser_relations

  binary.api.p2p_advertiser_relations()

.. seealso::
   * `Binary API Docs for p2p_advertiser_relations <https://developers.binary.com/api/#p2p_advertiser_relations>`_
    