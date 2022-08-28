
Transactions Stream (transaction)
==================================================================

Subscribe to transaction notifications

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: transaction(subscribe: Optional[Union[bool, int]], passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param subscribe: If set to 1, will send updates whenever there is an update to transactions. If not to 1 then it will not return any records.
   :type subscribe: Optional[Union[bool, int]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.transaction

  binary.api.transaction(
      subscribe=1
  )

.. seealso::
   * `Binary API Docs for transaction <https://developers.binary.com/api/#transaction>`_
    