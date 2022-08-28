
Portfolio (portfolio)
======================================================

Receive information about my current portfolio of outstanding options

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: portfolio(contract_type: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param contract_type: Return only contracts of the specified types
   :type contract_type: Optional[List]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.portfolio

  binary.api.portfolio()

.. seealso::
   * `Binary API Docs for portfolio <https://developers.binary.com/api/#portfolio>`_
    