
Cryptocurrency configurations (crypto_config)
==============================================================================

The request for cryptocurrencies configuration.




.. py:method:: crypto_config(currency_code: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param currency_code: [Optional] Cryptocurrency code. Sending request with currency_code provides crypto config for the sent cryptocurrency code only.
   :type currency_code: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.crypto_config

  binary.api.crypto_config()

.. seealso::
   * `Binary API Docs for crypto_config <https://developers.binary.com/api/#crypto_config>`_
    