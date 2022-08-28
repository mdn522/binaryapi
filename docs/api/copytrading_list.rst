
Copy Trading: List (copytrading_list)
======================================================================

Retrieves a list of active copiers and/or traders for Copy Trading

Auth Scope(s): :code:`admin`


.. py:method:: copytrading_list(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.copytrading_list

  binary.api.copytrading_list()

.. seealso::
   * `Binary API Docs for copytrading_list <https://developers.binary.com/api/#copytrading_list>`_
    