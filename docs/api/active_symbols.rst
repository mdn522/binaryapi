
Active Symbols (active_symbols)
================================================================

Retrieve a list of all currently active symbols (underlying markets upon which contracts are available for trading).




.. py:method:: active_symbols(active_symbols: str, landing_company: Optional[str] = None, product_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param active_symbols: If you use `brief`, only a subset of fields will be returned.
   :type active_symbols: str
   :param landing_company: [Optional] If you specify this field, only symbols available for trading by that landing company will be returned. If you are logged in, only symbols available for trading by your landing company will be returned regardless of what you specify in this field.
   :type landing_company: Optional[str]
   :param product_type: [Optional] If you specify this field, only symbols that can be traded through that product type will be returned.
   :type product_type: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.active_symbols

  binary.api.active_symbols(
      'brief'
      product_type='basic'
  )

.. seealso::
   * `Binary API Docs for active_symbols <https://developers.binary.com/api/#active_symbols>`_
    