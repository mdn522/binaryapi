
Set Account Currency (set_account_currency)
============================================================================

Set account currency, this will be default currency for your account i.e currency for trading, deposit. Please note that account currency can only be set once, and then can never be changed.

Auth Scope(s): :code:`admin`


.. py:method:: set_account_currency(set_account_currency: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param set_account_currency: Currency of the account. List of supported currencies can be acquired with `payout_currencies` call.
   :type set_account_currency: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.set_account_currency

  binary.api.set_account_currency(
      'USD'
  )

.. seealso::
   * `Binary API Docs for set_account_currency <https://developers.binary.com/api/#set_account_currency>`_
    