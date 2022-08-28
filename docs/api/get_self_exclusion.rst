
Get Self-Exclusion (get_self_exclusion)
========================================================================

Allows users to exclude themselves from the website for certain periods of time, or to set limits on their trading activities. This facility is a regulatory requirement for certain Landing Companies.

Auth Scope(s): :code:`read`


.. py:method:: get_self_exclusion(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.get_self_exclusion

  binary.api.get_self_exclusion()

.. seealso::
   * `Binary API Docs for get_self_exclusion <https://developers.binary.com/api/#get_self_exclusion>`_
    