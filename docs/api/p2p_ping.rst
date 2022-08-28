
P2P Ping (p2p_ping)
====================================================

Keeps the connection alive and updates the P2P advertiser's online status. The advertiser will be considered offline 60 seconds after a call is made.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_ping(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_ping

  binary.api.p2p_ping()

.. seealso::
   * `Binary API Docs for p2p_ping <https://developers.binary.com/api/#p2p_ping>`_
    