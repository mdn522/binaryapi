
Payment Methods (payment_methods)
==================================================================

Will return a list payment methods available for the given country. If the request is authenticated the client's residence country will be used.




.. py:method:: payment_methods(country: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param country: [Optional] 2-letter country code (ISO standard).
   :type country: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.payment_methods

  binary.api.payment_methods(
      country='id'
  )

.. seealso::
   * `Binary API Docs for payment_methods <https://developers.binary.com/api/#payment_methods>`_
    