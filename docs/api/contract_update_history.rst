
Update Contract History (contract_update_history)
==================================================================================

Request for contract update history.

Auth Scope(s): :code:`read`


.. py:method:: contract_update_history(contract_id: int, limit: Optional[Union[int, float, Decimal]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_id: Internal unique contract identifier.
   :type contract_id: int
   :param limit: [Optional] Maximum number of historical updates to receive.
   :type limit: Optional[Union[int, float, Decimal]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.contract_update_history

  binary.api.contract_update_history(
      contract_id=123
  )

.. seealso::
   * `Binary API Docs for contract_update_history <https://developers.binary.com/api/#contract_update_history>`_
    