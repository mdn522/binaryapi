
MT5: Get Setting (mt5_get_settings)
====================================================================

Get MT5 user account settings

Auth Scope(s): :code:`read`


.. py:method:: mt5_get_settings(login: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param login: MT5 user login
   :type login: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.mt5_get_settings

  binary.api.mt5_get_settings(
      login='MTR1000'
  )

.. seealso::
   * `Binary API Docs for mt5_get_settings <https://developers.binary.com/api/#mt5_get_settings>`_
    