
Contracts For Symbol (contracts_for)
=====================================================================

For a given symbol, get the list of currently available contracts, and the latest barrier and duration limits for each contract.




.. py:method:: contracts_for(contracts_for: str, currency: Optional[str] = None, landing_company: Optional[str] = None, product_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contracts_for: The short symbol name (obtained from `active_symbols` call).
   :type contracts_for: str
   :param currency: [Optional] Currency of the contract's stake and payout (obtained from `payout_currencies` call).
   :type currency: Optional[str]
   :param landing_company: [Optional] Indicates which landing company to get a list of contracts for. If you are logged in, your account's landing company will override this field.
   :type landing_company: Optional[str]
   :param product_type: [Optional] If you specify this field, only contracts tradable through that contract type will be returned.
   :type product_type: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.contracts_for

  binary.api.contracts_for(
      'R_50'
      currency='USD'
      landing_company='svg'
      product_type='basic'
  )

.. seealso::
   * `Binary API Docs for contracts_for <https://developers.binary.com/api/#contracts_for>`_
    