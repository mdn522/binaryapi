
Update Contract (contract_update)
==================================================================

Update a contract condition.

Auth Scope(s): :code:`trade`


.. py:method:: contract_update(contract_id: int, limit_order, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_id: Internal unique contract identifier.
   :type contract_id: int
   :param limit_order: Specify limit order to update.
   :type limit_order: 
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.contract_update

  binary.api.contract_update(
      contract_id=123
      limit_order={'take_profit': 1}
  )

.. seealso::
   * `Binary API Docs for contract_update <https://developers.binary.com/api/#contract_update>`_
    