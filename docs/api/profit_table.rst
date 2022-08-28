
Profit Table (profit_table)
============================================================

Retrieve a summary of account Profit Table, according to given search criteria

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: profit_table(contract_type: Optional[List] = None, date_from: Optional[str] = None, date_to: Optional[str] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, sort: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_type: Return only contracts of the specified types
   :type contract_type: Optional[List]
   :param date_from: [Optional] Start date (epoch or YYYY-MM-DD)
   :type date_from: Optional[str]
   :param date_to: [Optional] End date (epoch or YYYY-MM-DD)
   :type date_to: Optional[str]
   :param description: [Optional] If set to 1, will return full contracts description.
   :type description: Optional[int]
   :param limit: [Optional] Apply upper limit to count of transactions received.
   :type limit: Optional[Union[int, float, Decimal]]
   :param offset: [Optional] Number of transactions to skip.
   :type offset: Optional[Union[int, float, Decimal]]
   :param sort: [Optional] Sort direction.
   :type sort: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.profit_table

  binary.api.profit_table(
      description=1
      limit=25
      offset=25
      sort='ASC'
  )

.. seealso::
   * `Binary API Docs for profit_table <https://developers.binary.com/api/#profit_table>`_
    