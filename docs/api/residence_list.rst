
Countries List (residence_list)
================================================================

This call returns a list of countries and 2-letter country codes, suitable for populating the account opening form.




.. py:method:: residence_list(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.residence_list

  binary.api.residence_list()

.. seealso::
   * `Binary API Docs for residence_list <https://developers.binary.com/api/#residence_list>`_
    