
MT5: Accounts List (mt5_login_list)
====================================================================

Get list of MT5 accounts for client

Auth Scope(s): :code:`read`


.. py:method:: mt5_login_list(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.mt5_login_list

  binary.api.mt5_login_list()

.. seealso::
   * `Binary API Docs for mt5_login_list <https://developers.binary.com/api/#mt5_login_list>`_
    