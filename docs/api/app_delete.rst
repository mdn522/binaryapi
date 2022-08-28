
Application: Delete (app_delete)
=================================================================

The request for deleting an application.

Auth Scope(s): :code:`admin`


.. py:method:: app_delete(app_delete: int, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param app_delete: Application app_id
   :type app_delete: int
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.app_delete

  binary.api.app_delete(
      1234
  )

.. seealso::
   * `Binary API Docs for app_delete <https://developers.binary.com/api/#app_delete>`_
    