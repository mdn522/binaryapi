
Application: Get Details (app_get)
===================================================================

To get the information of the OAuth application specified by 'app_id'

Auth Scope(s): :code:`read`


.. py:method:: app_get(app_get: int, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param app_get: Application app_id
   :type app_get: int
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.app_get

  binary.api.app_get(
      1234
  )

.. seealso::
   * `Binary API Docs for app_get <https://developers.binary.com/api/#app_get>`_
    