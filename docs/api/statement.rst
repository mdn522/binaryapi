
Statement (statement)
======================================================

Retrieve a summary of account transactions, according to given search criteria

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: statement(action_type: Optional[str] = None, date_from: Optional[int] = None, date_to: Optional[int] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param action_type: [Optional] To filter the statement according to the type of transaction.
   :type action_type: Optional[str]
   :param date_from: [Optional] Start date (epoch)
   :type date_from: Optional[int]
   :param date_to: [Optional] End date (epoch)
   :type date_to: Optional[int]
   :param description: [Optional] If set to 1, will return full contracts description.
   :type description: Optional[int]
   :param limit: [Optional] Maximum number of transactions to receive.
   :type limit: Optional[Union[int, float, Decimal]]
   :param offset: [Optional] Number of transactions to skip.
   :type offset: Optional[Union[int, float, Decimal]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.statement

  binary.api.statement(
      description=1
      limit=100
      offset=25
  )

.. seealso::
   * `Binary API Docs for statement <https://developers.binary.com/api/#statement>`_
    