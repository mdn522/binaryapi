
P2P Payment Methods (p2p_payment_methods)
==========================================================================

List all P2P payment methods.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_payment_methods(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_payment_methods

  binary.api.p2p_payment_methods()

.. seealso::
   * `Binary API Docs for p2p_payment_methods <https://developers.binary.com/api/#p2p_payment_methods>`_
    