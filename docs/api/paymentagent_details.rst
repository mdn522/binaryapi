
Payment agent details (paymentagent_details)
=============================================================================

Gets client's payment agent details.

Auth Scope(s): :code:`admin`


.. py:method:: paymentagent_details(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.paymentagent_details

  binary.api.paymentagent_details()

.. seealso::
   * `Binary API Docs for paymentagent_details <https://developers.binary.com/api/#paymentagent_details>`_
    