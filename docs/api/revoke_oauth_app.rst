
Revoke Oauth Application (revoke_oauth_app)
============================================================================

Used for revoking access of particular app.

Auth Scope(s): :code:`admin`


.. py:method:: revoke_oauth_app(revoke_oauth_app: int, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param revoke_oauth_app: The application ID to revoke.
   :type revoke_oauth_app: int
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.revoke_oauth_app

  binary.api.revoke_oauth_app(
      1234
  )

.. seealso::
   * `Binary API Docs for revoke_oauth_app <https://developers.binary.com/api/#revoke_oauth_app>`_
    