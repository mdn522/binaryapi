
Terms and Conditions Approval (tnc_approval)
=============================================================================

To approve the latest version of terms and conditions.

Auth Scope(s): :code:`admin`


.. py:method:: tnc_approval(affiliate_coc_agreement: Optional[int] = None, ukgc_funds_protection: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param affiliate_coc_agreement: [Optional] For Affiliate's Code of Conduct Agreement.
   :type affiliate_coc_agreement: Optional[int]
   :param ukgc_funds_protection: [Optional] For `ASK_UK_FUNDS_PROTECTION` in `cashier`.
   :type ukgc_funds_protection: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.tnc_approval

  binary.api.tnc_approval()

.. seealso::
   * `Binary API Docs for tnc_approval <https://developers.binary.com/api/#tnc_approval>`_
    