
Sell Contract (sell)
=====================================================

Sell a Contract as identified from a previous `portfolio` call.

Auth Scope(s): :code:`trade`


.. py:method:: sell(sell: int, price: Union[int, float, Decimal], passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param sell: Pass contract_id received from the `portfolio` call.
   :type sell: int
   :param price: Minimum price at which to sell the contract, or `0` for 'sell at market'.
   :type price: Union[int, float, Decimal]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.sell

  binary.api.sell(
      11542203588
      price=500
  )

.. seealso::
   * `Binary API Docs for sell <https://developers.binary.com/api/#sell>`_
    