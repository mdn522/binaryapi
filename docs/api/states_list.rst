
States List (states_list)
==========================================================

For a given country, returns a list of States of that country. This is useful to populate the account opening form.




.. py:method:: states_list(states_list: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param states_list: Client's 2-letter country code (obtained from `residence_list` call)
   :type states_list: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.states_list

  binary.api.states_list(
      'id'
  )

.. seealso::
   * `Binary API Docs for states_list <https://developers.binary.com/api/#states_list>`_
    