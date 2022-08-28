
Account Limits (get_limits)
============================================================

Trading and Withdrawal Limits for a given user

Auth Scope(s): :code:`read`


.. py:method:: get_limits(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.get_limits

  binary.api.get_limits()

.. seealso::
   * `Binary API Docs for get_limits <https://developers.binary.com/api/#get_limits>`_
    