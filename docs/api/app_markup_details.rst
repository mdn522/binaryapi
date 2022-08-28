
Application: Markup Details (app_markup_details)
=================================================================================

Retrieve details of `app_markup` according to criteria specified.

Auth Scope(s): :code:`read`


.. py:method:: app_markup_details(date_from: str, date_to: str, app_id: Optional[int] = None, client_loginid: Optional[str] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, sort: Optional[str] = None, sort_fields: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param date_from: Start date (epoch or YYYY-MM-DD HH:MM:SS). Results are inclusive of this time.
   :type date_from: str
   :param date_to: End date (epoch or YYYY-MM-DD HH::MM::SS). Results are inclusive of this time.
   :type date_to: str
   :param app_id: [Optional] Specific application `app_id` to report on.
   :type app_id: Optional[int]
   :param client_loginid: [Optional] Specific client loginid to report on, like CR12345
   :type client_loginid: Optional[str]
   :param description: [Optional] If set to 1, will return `app_markup` transaction details.
   :type description: Optional[int]
   :param limit: [Optional] Apply upper limit to count of transactions received.
   :type limit: Optional[Union[int, float, Decimal]]
   :param offset: [Optional] Number of transactions to skip.
   :type offset: Optional[Union[int, float, Decimal]]
   :param sort: [Optional] Sort direction on `transaction_time`. Other fields sort order is ASC.
   :type sort: Optional[str]
   :param sort_fields: [Optional] One or more of the specified fields to sort on. Default sort field is by `transaction_time`.
   :type sort_fields: Optional[List]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.app_markup_details

  binary.api.app_markup_details(
      description=1
      app_id=1234
      client_loginid='CR12345'
      date_from='2017-08-01 00:00:00'
      date_to='2017-08-31 23:59:59'
      limit=100
      offset=0
      sort='ASC'
      sort_fields=['app_id', 'client_loginid', 'transaction_time']
      passthrough={}
      req_id=3
  )

.. seealso::
   * `Binary API Docs for app_markup_details <https://developers.binary.com/api/#app_markup_details>`_
    