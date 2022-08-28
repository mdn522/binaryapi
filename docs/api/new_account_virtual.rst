
New Virtual-Money Account (new_account_virtual)
================================================================================

Create a new virtual-money account.




.. py:method:: new_account_virtual(affiliate_token: Optional[str] = None, client_password: Optional[str] = None, date_first_contact: Optional[str] = None, email_consent: Optional[int] = None, gclid_url: Optional[str] = None, residence: Optional[str] = None, signup_device: Optional[str] = None, type: Optional[str] = None, utm_ad_id=None, utm_adgroup_id=None, utm_adrollclk_id=None, utm_campaign=None, utm_campaign_id=None, utm_content=None, utm_fbcl_id=None, utm_gl_client_id=None, utm_medium=None, utm_msclk_id=None, utm_source=None, utm_term=None, verification_code: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param affiliate_token: [Optional] Affiliate token, within 32 characters.
   :type affiliate_token: Optional[str]
   :param client_password: Password (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
   :type client_password: Optional[str]
   :param date_first_contact: [Optional] Date of first contact, format: `yyyy-mm-dd` in GMT timezone.
   :type date_first_contact: Optional[str]
   :param email_consent: [Optional] Boolean value: 1 or 0, indicating whether the client has given consent for marketing emails.
   :type email_consent: Optional[int]
   :param gclid_url: [Optional] Google Click Identifier to track source.
   :type gclid_url: Optional[str]
   :param residence: 2-letter country code (obtained from `residence_list` call).
   :type residence: Optional[str]
   :param signup_device: [Optional] Show whether user has used mobile or desktop.
   :type signup_device: Optional[str]
   :param type: Account type
   :type type: Optional[str]
   :param utm_ad_id: [Optional] Identifier of particular ad. Value must match Regex pattern to be recorded
   :type utm_ad_id: 
   :param utm_adgroup_id: [Optional] Identifier of ad group in the campaign. Value must match Regex pattern to be recorded
   :type utm_adgroup_id: 
   :param utm_adrollclk_id: [Optional] Unique identifier of click on AdRoll ads platform. Value must match Regex pattern to be recorded
   :type utm_adrollclk_id: 
   :param utm_campaign: [Optional] Identifies a specific product promotion or strategic campaign such as a spring sale or other promotions. Value must match Regex pattern to be recorded
   :type utm_campaign: 
   :param utm_campaign_id: [Optional] Identifier of paid ad campaign. Value must match Regex pattern to be recorded
   :type utm_campaign_id: 
   :param utm_content: [Optional] Used to differentiate similar content, or links within the same ad. Value must match Regex pattern to be recorded
   :type utm_content: 
   :param utm_fbcl_id: [Optional] Unique identifier of click on Facebook ads platform. Value must match Regex pattern to be recorded
   :type utm_fbcl_id: 
   :param utm_gl_client_id: [Optional] Unique visitor identifier on Google Ads platform. Value must match Regex pattern to be recorded
   :type utm_gl_client_id: 
   :param utm_medium: [Optional] Identifies the medium the link was used upon such as: email, CPC, or other methods of sharing. Value must match Regex pattern to be recorded
   :type utm_medium: 
   :param utm_msclk_id: [Optional] Unique click identifier on Microsoft Bing ads platform. Value must match Regex pattern to be recorded
   :type utm_msclk_id: 
   :param utm_source: [Optional] Identifies the source of traffic such as: search engine, newsletter, or other referral. Value must match Regex pattern to be recorded
   :type utm_source: 
   :param utm_term: [Optional] Used to send information related to the campaign term like paid search keywords. Value must match Regex pattern to be recorded
   :type utm_term: 
   :param verification_code: Email verification code (received from a `verify_email` call, which must be done first).
   :type verification_code: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.new_account_virtual

  binary.api.new_account_virtual(
      type='trading'
      client_password='C0rrect_p4ssword'
      residence='id'
      verification_code='uoJvVuQ6'
  )

.. seealso::
   * `Binary API Docs for new_account_virtual <https://developers.binary.com/api/#new_account_virtual>`_
    