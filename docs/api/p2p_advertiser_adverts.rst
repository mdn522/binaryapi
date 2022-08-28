
P2P Advertiser Adverts (p2p_advertiser_adverts)
================================================================================

Returns all P2P adverts created by the authorized client. Can only be used by a registered P2P advertiser.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_adverts(limit: Optional[int] = None, offset: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param limit: [Optional] Used for paging. This value will also apply to subsription responses.
   :type limit: Optional[int]
   :param offset: [Optional] Used for paging. This value will also apply to subsription responses.
   :type offset: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advertiser_adverts

  binary.api.p2p_advertiser_adverts()

.. seealso::
   * `Binary API Docs for p2p_advertiser_adverts <https://developers.binary.com/api/#p2p_advertiser_adverts>`_
    