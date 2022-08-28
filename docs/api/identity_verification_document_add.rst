
Identity Verification Add Document (identity_verification_document_add)
========================================================================================================

Adds document information such as issuing country, id and type for identity verification processes.

Auth Scope(s): :code:`admin`


.. py:method:: identity_verification_document_add(document_number: str, document_type: str, issuing_country: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param document_number: The identification number of the document.
   :type document_number: str
   :param document_type: The type of the document based on provided `issuing_country` (can obtained from `residence_list` call).
   :type document_type: str
   :param issuing_country: 2-letter country code (can obtained from `residence_list` call).
   :type issuing_country: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.identity_verification_document_add

  binary.api.identity_verification_document_add(
      document_number='12345678912'
      document_type='nin_slip'
      issuing_country='ng'
  )

.. seealso::
   * `Binary API Docs for identity_verification_document_add <https://developers.binary.com/api/#identity_verification_document_add>`_
    