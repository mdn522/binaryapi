
Verify Email (verify_email)
============================================================

Verify an email address for various purposes. The system will send an email to the address containing a security code for verification.




.. py:method:: verify_email(verify_email: str, type: str, url_parameters=None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param verify_email: Email address to be verified.
   :type verify_email: str
   :param type: Purpose of the email verification call.
   :type type: str
   :param url_parameters: [Optional] Extra parameters that can be attached to the verify email link URL.
   :type url_parameters: 
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.verify_email

  binary.api.verify_email(
      'test@mailinator.com'
      type='account_opening'
  )

.. seealso::
   * `Binary API Docs for verify_email <https://developers.binary.com/api/#verify_email>`_
    