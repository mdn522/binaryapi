
P2P Advert Information (p2p_advert_info)
=========================================================================

Retrieve information about a P2P advert.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advert_info(id: Optional[str] = None, subscribe: Optional[Union[bool, int]] = None, use_client_limits: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param id: [Optional] The unique identifier for this advert. Optional when subscribe is 1. If not provided, all advertiser adverts will be subscribed.
   :type id: Optional[str]
   :param subscribe: [Optional] If set to 1, will send updates when changes occur. Optional when id is provided.
   :type subscribe: Optional[Union[bool, int]]
   :param use_client_limits: [Optional] If set to 1, the maximum order amount will be adjusted to the current balance and turnover limits of the account.
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
  :name: binary.api.p2p_advert_info

  binary.api.p2p_advert_info(
      id='1234'
  )

.. seealso::
   * `Binary API Docs for p2p_advert_info <https://developers.binary.com/api/#p2p_advert_info>`_
    