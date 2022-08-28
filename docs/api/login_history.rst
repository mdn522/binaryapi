
Login History (login_history)
==============================================================

Retrieve a summary of login history for user.

Auth Scope(s): :code:`read`


.. py:method:: login_history(limit: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param limit: [Optional] Apply limit to count of login history records.
   :type limit: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.login_history

  binary.api.login_history(
      limit=25
  )

.. seealso::
   * `Binary API Docs for login_history <https://developers.binary.com/api/#login_history>`_
    