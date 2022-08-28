
OAuth Applications (oauth_apps)
================================================================

List all my used OAuth applications.

Auth Scope(s): :code:`read`


.. py:method:: oauth_apps(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.oauth_apps

  binary.api.oauth_apps()

.. seealso::
   * `Binary API Docs for oauth_apps <https://developers.binary.com/api/#oauth_apps>`_
    