
Reality Check (reality_check)
==============================================================

Retrieve summary of client's trades and account for the Reality Check facility. A 'reality check' means a display of time elapsed since the session began, and associated client profit/loss. The Reality Check facility is a regulatory requirement for certain landing companies.

Auth Scope(s): :code:`read`, :code:`trading_information`


.. py:method:: reality_check(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.reality_check

  binary.api.reality_check()

.. seealso::
   * `Binary API Docs for reality_check <https://developers.binary.com/api/#reality_check>`_
    