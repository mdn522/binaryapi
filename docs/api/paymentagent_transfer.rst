
Payment Agent: Transfer (paymentagent_transfer)
================================================================================

Payment Agent Transfer - this call is available only to accounts that are approved Payment Agents.

Auth Scope(s): :code:`payments`


.. py:method:: paymentagent_transfer(amount: Union[int, float, Decimal], currency: str, transfer_to: str, description: Optional[str] = None, dry_run: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param amount: The amount to transfer.
   :type amount: Union[int, float, Decimal]
   :param currency: Currency code.
   :type currency: str
   :param transfer_to: The loginid of the recipient account.
   :type transfer_to: str
   :param description: [Optional] Remarks about the transfer.
   :type description: Optional[str]
   :param dry_run: [Optional] If set to `1`, just do validation.
   :type dry_run: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.paymentagent_transfer

  binary.api.paymentagent_transfer(
      amount=1000
      currency='USD'
      transfer_to='CR100001'
  )

.. seealso::
   * `Binary API Docs for paymentagent_transfer <https://developers.binary.com/api/#paymentagent_transfer>`_
    