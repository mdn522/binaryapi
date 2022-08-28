
P2P Advertiser Information (p2p_advertiser_info)
=================================================================================

Retrieve information about a P2P advertiser.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_info(id: Optional[str] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param id: [Optional] The unique identifier for this advertiser. If not provided, returns advertiser information about the current account.
   :type id: Optional[str]
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
  :name: binary.api.p2p_advertiser_info

  binary.api.p2p_advertiser_info()

.. seealso::
   * `Binary API Docs for p2p_advertiser_info <https://developers.binary.com/api/#p2p_advertiser_info>`_
    