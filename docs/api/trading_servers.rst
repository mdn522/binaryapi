
Server list (trading_servers)
==============================================================

Get the list of servers for a trading platform.

Auth Scope(s): :code:`read`


.. py:method:: trading_servers(account_type: Optional[str] = None, environment: Optional[str] = None, market_type: Optional[str] = None, platform: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param account_type: [Optional] Trading account type.
   :type account_type: Optional[str]
   :param environment: [Optional] Pass the environment (installation) instance. Currently, there are one demo and two real environments. Defaults to 'all'.
   :type environment: Optional[str]
   :param market_type: [Optional] Market type.
   :type market_type: Optional[str]
   :param platform: [Optional] Pass the trading platform name, default to mt5
   :type platform: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.trading_servers

  binary.api.trading_servers(
      platform='mt5'
  )

.. seealso::
   * `Binary API Docs for trading_servers <https://developers.binary.com/api/#trading_servers>`_
    