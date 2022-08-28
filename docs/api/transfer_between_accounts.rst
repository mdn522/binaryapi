
Transfer Between Accounts (transfer_between_accounts)
======================================================================================

This call allows transfers between accounts held by a given user. Transfer funds between your fiat and cryptocurrency accounts (for a fee). Please note that account_from should be same as current authorized account.

Auth Scope(s): :code:`payments`


.. py:method:: transfer_between_accounts(account_from: Optional[str] = None, account_to: Optional[str] = None, accounts: Optional[str] = None, amount: Optional[Union[int, float, Decimal]] = None, currency: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param account_from: [Optional] The loginid of the account to transfer funds from.
   :type account_from: Optional[str]
   :param account_to: [Optional] The loginid of the account to transfer funds to.
   :type account_to: Optional[str]
   :param accounts: [Optional] To control the list of accounts returned when `account_from` or `account_to` is not provided. `brief` (default value) means that accounts with `mt5` account_type will be excluded; it will run faster. `all` means that all accounts with any account_type (including `mt5`) will be returned.
   :type accounts: Optional[str]
   :param amount: [Optional] The amount to transfer.
   :type amount: Optional[Union[int, float, Decimal]]
   :param currency: [Optional] Currency code.
   :type currency: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.transfer_between_accounts

  binary.api.transfer_between_accounts(
      account_from='MLT100'
      account_to='MF100'
      amount=1000
      currency='EUR'
  )

.. seealso::
   * `Binary API Docs for transfer_between_accounts <https://developers.binary.com/api/#transfer_between_accounts>`_
    