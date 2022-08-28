
Server Status (website_status)
===============================================================

Request server status.




.. py:method:: website_status(subscribe: Optional[Union[bool, int]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param subscribe: [Optional] `1` to stream the server/website status updates.
   :type subscribe: Optional[Union[bool, int]]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.website_status

  binary.api.website_status()

.. seealso::
   * `Binary API Docs for website_status <https://developers.binary.com/api/#website_status>`_
    