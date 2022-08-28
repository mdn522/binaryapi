
Payout Currencies (payout_currencies)
======================================================================

Retrieve a list of available option payout currencies. If a user is logged in, only the currencies available for the account will be returned.




.. py:method:: payout_currencies(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.payout_currencies

  binary.api.payout_currencies()

.. seealso::
   * `Binary API Docs for payout_currencies <https://developers.binary.com/api/#payout_currencies>`_
    