
Exchange Rates (exchange_rates)
================================================================

Retrieves the exchange rates from a base currency to all currencies supported by the system.




.. py:method:: exchange_rates(base_currency: str, subscribe: Optional[Union[bool, int]] = None, target_currency: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param base_currency: Base currency (can be obtained from `payout_currencies` call)
   :type base_currency: str
   :param subscribe: [Optional] 1 - to initiate a realtime stream of exchange rates relative to base currency.
   :type subscribe: Optional[Union[bool, int]]
   :param target_currency: [Optional] Local currency
   :type target_currency: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.exchange_rates

  binary.api.exchange_rates(
      base_currency='USD'
  )

.. seealso::
   * `Binary API Docs for exchange_rates <https://developers.binary.com/api/#exchange_rates>`_
    