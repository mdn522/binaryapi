
Authorize (authorize)
======================================================

Authorize current WebSocket session to act on behalf of the owner of a given token. Must precede requests that need to access client account, for example purchasing and selling contracts or viewing portfolio.




.. py:method:: authorize(authorize: str, add_to_login_history: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param authorize: Authentication token. May be retrieved from https://www.binary.com/en/user/security/api_tokenws.html
   :type authorize: str
   :param add_to_login_history: [Optional] Send this when you use api tokens for authorization and want to track activity using `login_history` call.
   :type add_to_login_history: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.authorize

  binary.api.authorize(
      'uw2mk7no3oktoRVVsB4Dz7TQncfABuFDgO95dlxfMxRuPUDz'
  )

.. seealso::
   * `Binary API Docs for authorize <https://developers.binary.com/api/#authorize>`_
    