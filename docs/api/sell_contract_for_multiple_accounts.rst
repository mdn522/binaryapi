
Sell Contracts: Multiple Accounts (sell_contract_for_multiple_accounts)
========================================================================================================

Sell contracts for multiple accounts simultaneously. Uses the shortcode response from `buy_contract_for_multiple_accounts` to identify the contract, and authorisation tokens to select which accounts to sell those contracts on. Note that only the accounts identified by the tokens will be affected. This will not sell the contract on the currently-authorised account unless you include the token for the current account.

Auth Scope(s): :code:`trade`


.. py:method:: sell_contract_for_multiple_accounts(price: Union[int, float, Decimal], shortcode: str, tokens: List, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param price: Minimum price at which to sell the contract, or `0` for 'sell at market'.
   :type price: Union[int, float, Decimal]
   :param shortcode: An internal ID used to identify the contract which was originally bought. This is returned from the `buy` and `buy_contract_for_multiple_accounts` calls.
   :type shortcode: str
   :param tokens: Authorisation tokens which select the accounts to sell use for the affected accounts.
   :type tokens: List
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.sell_contract_for_multiple_accounts

  binary.api.sell_contract_for_multiple_accounts(
      price=500
      shortcode='CALL_R_50_5_1488181433_1488181553_S0P_0'
      tokens=['FrvservuIFEf1', 'JUBibibkebiuwbeCNEc']
  )

.. seealso::
   * `Binary API Docs for sell_contract_for_multiple_accounts <https://developers.binary.com/api/#sell_contract_for_multiple_accounts>`_
    