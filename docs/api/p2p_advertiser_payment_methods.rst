
P2P Advertiser Payment Methods (p2p_advertiser_payment_methods)
================================================================================================

Manage or list P2P advertiser payment methods.

Auth Scope(s): :code:`payments`


.. py:method:: p2p_advertiser_payment_methods(create: Optional[List] = None, delete: Optional[List] = None, update=None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param create: Contains new payment method entries.
   :type create: Optional[List]
   :param delete: Contains payment methods to delete.
   :type delete: Optional[List]
   :param update: Contains payment methods to update.
   :type update: 
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.p2p_advertiser_payment_methods

  binary.api.p2p_advertiser_payment_methods(
      create=[{'account': '1234', 'bank_name': 'some_bank', 'method': 'bank_transfer'}]
      delete=[101, 102]
      update={'103': {'instructions': 'phone first'}}
  )

.. seealso::
   * `Binary API Docs for p2p_advertiser_payment_methods <https://developers.binary.com/api/#p2p_advertiser_payment_methods>`_
    