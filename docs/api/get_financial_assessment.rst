
Get Financial Assessment (get_financial_assessment)
====================================================================================

This call gets the financial assessment details. The 'financial assessment' is a questionnaire that clients of certain Landing Companies need to complete, due to regulatory and KYC (know your client) requirements.

Auth Scope(s): :code:`read`


.. py:method:: get_financial_assessment(passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.get_financial_assessment

  binary.api.get_financial_assessment()

.. seealso::
   * `Binary API Docs for get_financial_assessment <https://developers.binary.com/api/#get_financial_assessment>`_
    