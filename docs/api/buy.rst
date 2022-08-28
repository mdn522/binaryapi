
Buy Contract (buy)
===================================================

Buy a Contract

Auth Scope(s): :code:`trade`


.. py:method:: buy(buy: str, price: Union[int, float, Decimal], parameters=None, subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param buy: Either the ID received from a Price Proposal (`proposal` call), or `1` if contract buy parameters are passed in the `parameters` field.
   :type buy: str
   :param price: Maximum price at which to purchase the contract.
   :type price: Union[int, float, Decimal]
   :param parameters: [Optional] Used to pass the parameters for contract buy.
   :type parameters: 
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
  :name: binary.api.buy

  binary.api.buy(
      'uw2mk7no3oktoRVVsB4Dz7TQnFfABuFDgO95dlxfMxRuPUsz'
      price=100
  )

.. seealso::
   * `Binary API Docs for buy <https://developers.binary.com/api/#buy>`_
    