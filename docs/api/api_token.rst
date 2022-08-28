
API Token (api_token)
======================================================

This call manages API tokens

Auth Scope(s): :code:`admin`


.. py:method:: api_token(delete_token: Optional[str] = None, new_token: Optional[str] = None, new_token_scopes: Optional[List] = None, valid_for_current_ip_only: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param delete_token: [Optional] The token to remove.
   :type delete_token: Optional[str]
   :param new_token: [Optional] The name of the created token.
   :type new_token: Optional[str]
   :param new_token_scopes: [Optional] List of permission scopes to provide with the token.
   :type new_token_scopes: Optional[List]
   :param valid_for_current_ip_only: [Optional] If you set this parameter during token creation, then the token created will only work for the IP address that was used to create the token
   :type valid_for_current_ip_only: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.api_token

  binary.api.api_token(
      new_token='Token example'
      new_token_scopes=['admin', 'read', 'trade']
  )

.. seealso::
   * `Binary API Docs for api_token <https://developers.binary.com/api/#api_token>`_
    