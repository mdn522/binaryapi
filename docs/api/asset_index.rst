
Asset Index (asset_index)
==========================================================

Retrieve a list of all available underlyings and the corresponding contract types and duration boundaries. If the user is logged in, only the assets available for that user's landing company will be returned.




.. py:method:: asset_index(landing_company: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param landing_company: [Optional] If specified, will return only the underlyings for the specified landing company.
   :type landing_company: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.asset_index

  binary.api.asset_index()

.. seealso::
   * `Binary API Docs for asset_index <https://developers.binary.com/api/#asset_index>`_
    