
Landing Company (landing_company)
==================================================================

The company has a number of licensed subsidiaries in various jurisdictions, which are called Landing Companies. This call will return the appropriate Landing Company for clients of a given country. The landing company may differ for Gaming contracts (Synthetic Indices) and Financial contracts (Forex, Stock Indices, Commodities).




.. py:method:: landing_company(landing_company: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param landing_company: Client's 2-letter country code (obtained from `residence_list` call).
   :type landing_company: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.landing_company

  binary.api.landing_company(
      'id'
  )

.. seealso::
   * `Binary API Docs for landing_company <https://developers.binary.com/api/#landing_company>`_
    