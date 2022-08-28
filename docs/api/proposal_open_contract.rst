
Price Proposal: Open Contracts (proposal_open_contract)
========================================================================================

Get latest price (and other information) for a contract in the user's portfolio

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: proposal_open_contract(contract_id: Optional[int] = None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_id: [Optional] Contract ID received from a `portfolio` request. If not set, you will receive stream of all open contracts.
   :type contract_id: Optional[int]
   :param subscribe: [Optional] `1` to stream.
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
  :name: binary.api.proposal_open_contract

  binary.api.proposal_open_contract(
      contract_id=11111111
      subscribe=1
  )

.. seealso::
   * `Binary API Docs for proposal_open_contract <https://developers.binary.com/api/#proposal_open_contract>`_
    