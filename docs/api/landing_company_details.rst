
Landing Company Details (landing_company_details)
==================================================================================

The company has a number of licensed subsidiaries in various jurisdictions, which are called Landing Companies (and which are wholly owned subsidiaries of the Deriv Group). This call provides information about each Landing Company.




.. py:method:: landing_company_details(landing_company_details: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param landing_company_details: Landing company shortcode.
   :type landing_company_details: str
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.landing_company_details

  binary.api.landing_company_details(
      'svg'
  )

.. seealso::
   * `Binary API Docs for landing_company_details <https://developers.binary.com/api/#landing_company_details>`_
    