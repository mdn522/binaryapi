
Application: List (app_list)
=============================================================

List all of the account's OAuth applications

Auth Scope(s): :code:`read`


.. py:method:: app_list(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.app_list

  binary.api.app_list()

.. seealso::
   * `Binary API Docs for app_list <https://developers.binary.com/api/#app_list>`_
    