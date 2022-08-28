
Price Proposal (proposal)
==========================================================

Gets latest price for a specific contract.




.. py:method:: proposal(contract_type: str, currency: str, symbol: str, amount: Optional[Union[int, float, Decimal]] = None, barrier: Optional[str] = None, barrier2: Optional[str] = None, barrier_range: Optional[str] = None, basis: Optional[str] = None, cancellation: Optional[str] = None, date_expiry: Optional[int] = None, date_start: Optional[int] = None, duration: Optional[int] = None, duration_unit: Optional[str] = None, limit_order=None, multiplier: Optional[Union[int, float, Decimal]] = None, product_type: Optional[str] = None, selected_tick: Optional[int] = None, subscribe: Optional[Union[bool, int]] = None, trading_period_start: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_type: The proposed contract type
   :type contract_type: str
   :param currency: This can only be the account-holder's currency (obtained from `payout_currencies` call).
   :type currency: str
   :param symbol: The short symbol name (obtained from `active_symbols` call).
   :type symbol: str
   :param amount: [Optional] Proposed contract payout or stake, or multiplier (for lookbacks).
   :type amount: Optional[Union[int, float, Decimal]]
   :param barrier: [Optional] Barrier for the contract (or last digit prediction for digit contracts). Contracts less than 24 hours in duration would need a relative barrier (barriers which need +/-), where entry spot would be adjusted accordingly with that amount to define a barrier, except for Synthetic Indices as they support both relative and absolute barriers. Not needed for lookbacks.
   :type barrier: Optional[str]
   :param barrier2: [Optional] Low barrier for the contract (for contracts with two barriers). Contracts less than 24 hours in duration would need a relative barrier (barriers which need +/-), where entry spot would be adjusted accordingly with that amount to define a barrier, except for Synthetic Indices as they support both relative and absolute barriers. Not needed for lookbacks.
   :type barrier2: Optional[str]
   :param barrier_range: [Optional] Barrier range for callputspread.
   :type barrier_range: Optional[str]
   :param basis: [Optional] Indicates type of the `amount`.
   :type basis: Optional[str]
   :param cancellation: Cancellation duration option (only for `MULTUP` and `MULTDOWN` contracts).
   :type cancellation: Optional[str]
   :param date_expiry: [Optional] Epoch value of the expiry time of the contract. Either date_expiry or duration is required.
   :type date_expiry: Optional[int]
   :param date_start: [Optional] Indicates epoch value of the starting time of the contract. If left empty, the start time of the contract is now.
   :type date_start: Optional[int]
   :param duration: [Optional] Duration quantity. Either date_expiry or duration is required.
   :type duration: Optional[int]
   :param duration_unit: [Optional] Duration unit - `s`: seconds, `m`: minutes, `h`: hours, `d`: days, `t`: ticks.
   :type duration_unit: Optional[str]
   :param limit_order: Add an order to close the contract once the order condition is met (only for `MULTUP` and `MULTDOWN` contracts). Supported orders: `take_profit`, `stop_loss`.
   :type limit_order: 
   :param multiplier: [Optional] The multiplier for non-binary options. E.g. lookbacks.
   :type multiplier: Optional[Union[int, float, Decimal]]
   :param product_type: [Optional] The product type.
   :type product_type: Optional[str]
   :param selected_tick: [Optional] The tick that is predicted to have the highest/lowest value - for `TICKHIGH` and `TICKLOW` contracts.
   :type selected_tick: Optional[int]
   :param subscribe: [Optional] 1 - to initiate a realtime stream of prices. Note that tick trades (without a user-defined barrier), digit trades and less than 24 hours at-the-money contracts for the following underlying symbols are not streamed: `R_10`, `R_25`, `R_50`, `R_75`, `R_100`, `RDBULL`, `RDBEAR` (this is because their price is constant).
   :type subscribe: Optional[Union[bool, int]]
   :param trading_period_start: [Optional] Required only for multi-barrier trading. Defines the epoch value of the trading period start time.
   :type trading_period_start: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.proposal

  binary.api.proposal(
      amount=100
      barrier='+0.1'
      basis='payout'
      contract_type='CALL'
      currency='USD'
      duration=60
      duration_unit='s'
      symbol='R_100'
  )

.. seealso::
   * `Binary API Docs for proposal <https://developers.binary.com/api/#proposal>`_
    