
Top Up Virtual-Money Account (topup_virtual)
=============================================================================

When a virtual-money's account balance becomes low, it can be topped up using this call.

Auth Scope(s): :code:`trade`


.. py:method:: topup_virtual(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.topup_virtual

  binary.api.topup_virtual()

.. seealso::
   * `Binary API Docs for topup_virtual <https://developers.binary.com/api/#topup_virtual>`_
    