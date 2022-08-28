
Application: Update (app_update)
=================================================================

Update a new OAuth application

Auth Scope(s): :code:`admin`


.. py:method:: app_update(app_update: int, name: str, scopes: List, app_markup_percentage: Optional[Union[int, float, Decimal]] = None, appstore: Optional[str] = None, github: Optional[str] = None, googleplay: Optional[str] = None, homepage: Optional[str] = None, redirect_uri: Optional[str] = None, verification_uri: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param app_update: Application app_id.
   :type app_update: int
   :param name: Application name.
   :type name: str
   :param scopes: Change scopes will revoke all user's grants and log them out.
   :type scopes: List
   :param app_markup_percentage: [Optional] Markup to be added to contract prices (as a percentage of contract payout).
   :type app_markup_percentage: Optional[Union[int, float, Decimal]]
   :param appstore: [Optional] Application's App Store URL (if applicable).
   :type appstore: Optional[str]
   :param github: [Optional] Application's GitHub page (for open-source projects).
   :type github: Optional[str]
   :param googleplay: [Optional] Application's Google Play URL (if applicable).
   :type googleplay: Optional[str]
   :param homepage: [Optional] Application's homepage URL.
   :type homepage: Optional[str]
   :param redirect_uri: [Optional] The URL to redirect to after a successful login. Required if charging markup percentage.
   :type redirect_uri: Optional[str]
   :param verification_uri: [Optional] Used when `verify_email` called. If available, a URL containing the verification token will send to the client's email, otherwise only the token will be sent.
   :type verification_uri: Optional[str]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.app_update

  binary.api.app_update(
      999
      appstore='https://itunes.apple.com/test_app'
      github='https://github.com/test_org/app'
      googleplay='https://play.google.com/store/apps/details?id=test.app'
      homepage='https://test.example.com/'
      name='Test Application'
      redirect_uri='https://test.example.com/redirect'
      scopes=['read', 'trade']
      verification_uri='https://test.example.com/verify'
  )

.. seealso::
   * `Binary API Docs for app_update <https://developers.binary.com/api/#app_update>`_
    