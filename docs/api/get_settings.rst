
Get Account Settings (get_settings)
====================================================================

Get User Settings (email, date of birth, address etc)

Auth Scope(s): :code:`read`


.. py:method:: get_settings(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.get_settings

  binary.api.get_settings()

.. seealso::
   * `Binary API Docs for get_settings <https://developers.binary.com/api/#get_settings>`_
    