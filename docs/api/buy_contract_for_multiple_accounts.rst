
Buy Contract for Multiple Accounts (buy_contract_for_multiple_accounts)
========================================================================================================

Buy a Contract for multiple Accounts specified by the `tokens` parameter. Note, although this is an authorized call, the contract is not bought for the authorized account.

Auth Scope(s): :code:`trade`


.. py:method:: buy_contract_for_multiple_accounts(buy_contract_for_multiple_accounts: str, price: Union[int, float, Decimal], tokens: List, parameters=None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param buy_contract_for_multiple_accounts: Either the ID received from a Price Proposal (`proposal` call), or `1` if contract buy parameters are passed in the `parameters` field.
   :type buy_contract_for_multiple_accounts: str
   :param price: Maximum price at which to purchase the contract.
   :type price: Union[int, float, Decimal]
   :param tokens: List of API tokens identifying the accounts for which the contract is bought. Note: If the same token appears multiple times or if multiple tokens designate the same account, the contract is bought multiple times for this account.
   :type tokens: List
   :param parameters: [Optional] Used to pass the parameters for contract buy.
   :type parameters: 
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.buy_contract_for_multiple_accounts

  binary.api.buy_contract_for_multiple_accounts(
      'AE79667A-3561-11E6-880B-19CE0BCBE464'
      price=2.57
      tokens=['EWHdv7feGJRmMf1kqv79lgfPiGjLLGV9GHTZFQ345FzJSfNE', 'ONqj76yAnVKnPtc', 'oSpp7ohpGf50tP6', 'uz6OSIcFIcPKK5T']
  )

.. seealso::
   * `Binary API Docs for buy_contract_for_multiple_accounts <https://developers.binary.com/api/#buy_contract_for_multiple_accounts>`_
    