
Economic Calendar (economic_calendar)
======================================================================

Specify a currency to receive a list of events related to that specific currency. For example, specifying USD will return a list of USD-related events. If the currency is omitted, you will receive a list for all currencies.




.. py:method:: economic_calendar(currency: Optional[str] = None, end_date: Optional[int] = None, start_date: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param currency: [Optional] Currency symbol.
   :type currency: Optional[str]
   :param end_date: [Optional] End date.
   :type end_date: Optional[int]
   :param start_date: [Optional] Start date.
   :type start_date: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.economic_calendar

  binary.api.economic_calendar(
      currency='USD'
      end_date=1561196696
      start_date=1561096696
  )

.. seealso::
   * `Binary API Docs for economic_calendar <https://developers.binary.com/api/#economic_calendar>`_
    