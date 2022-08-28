
Set Self-Exclusion (set_self_exclusion)
========================================================================

Set Self-Exclusion (this call should be used in conjunction with `get_self_exclusion`)

Auth Scope(s): :code:`admin`


.. py:method:: set_self_exclusion(exclude_until: Optional[str] = None, max_30day_deposit: Optional[Union[int, float, Decimal]] = None, max_30day_losses: Optional[Union[int, float, Decimal]] = None, max_30day_turnover: Optional[Union[int, float, Decimal]] = None, max_7day_deposit: Optional[Union[int, float, Decimal]] = None, max_7day_losses: Optional[Union[int, float, Decimal]] = None, max_7day_turnover: Optional[Union[int, float, Decimal]] = None, max_balance: Optional[Union[int, float, Decimal]] = None, max_deposit: Optional[Union[int, float, Decimal]] = None, max_losses: Optional[Union[int, float, Decimal]] = None, max_open_bets: Optional[int] = None, max_turnover: Optional[Union[int, float, Decimal]] = None, session_duration_limit: Optional[int] = None, timeout_until: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None) -> int

   :param exclude_until: [Optional] Exclude me from the website (for a minimum of 6 months, up to a maximum of 5 years). Note: uplifting this self-exclusion may require contacting the company.
   :type exclude_until: Optional[str]
   :param max_30day_deposit: [Optional] 7-day limit on deposits.
   :type max_30day_deposit: Optional[Union[int, float, Decimal]]
   :param max_30day_losses: [Optional] 30-day limit on losses.
   :type max_30day_losses: Optional[Union[int, float, Decimal]]
   :param max_30day_turnover: [Optional] 30-day turnover limit.
   :type max_30day_turnover: Optional[Union[int, float, Decimal]]
   :param max_7day_deposit: [Optional] 7-day limit on deposits.
   :type max_7day_deposit: Optional[Union[int, float, Decimal]]
   :param max_7day_losses: [Optional] 7-day limit on losses.
   :type max_7day_losses: Optional[Union[int, float, Decimal]]
   :param max_7day_turnover: [Optional] 7-day turnover limit.
   :type max_7day_turnover: Optional[Union[int, float, Decimal]]
   :param max_balance: [Optional] Maximum account cash balance.
   :type max_balance: Optional[Union[int, float, Decimal]]
   :param max_deposit: [Optional] Daily deposit limit.
   :type max_deposit: Optional[Union[int, float, Decimal]]
   :param max_losses: [Optional] Daily limit on losses.
   :type max_losses: Optional[Union[int, float, Decimal]]
   :param max_open_bets: [Optional] Maximum number of open positions.
   :type max_open_bets: Optional[int]
   :param max_turnover: [Optional] Daily turnover limit.
   :type max_turnover: Optional[Union[int, float, Decimal]]
   :param session_duration_limit: [Optional] Session duration limit, in minutes.
   :type session_duration_limit: Optional[int]
   :param timeout_until: [Optional] Exclude me from the website (for up to 6 weeks). Requires time in epoch format. Note: unlike `exclude_until`, this self-exclusion will be lifted automatically at the expiry of the timeout period.
   :type timeout_until: Optional[int]
   :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
   :type passthrough: Optional[Any]
   :param req_id: [Optional] Used to map request to response.
   :type req_id: Optional[int]
   :returns: req_id
   :rtype: int


Example
"""""""

.. code-block:: python
  :name: binary.api.set_self_exclusion

  binary.api.set_self_exclusion(
      exclude_until='2020-01-01'
      max_30day_deposit=1000
      max_30day_losses=100000
      max_30day_turnover=1000
      max_7day_deposit=100
      max_7day_losses=100000
      max_7day_turnover=1000
      max_deposit=10
      max_losses=100000
      max_turnover=1000
      session_duration_limit=3600
      timeout_until=1497357184
  )

.. seealso::
   * `Binary API Docs for set_self_exclusion <https://developers.binary.com/api/#set_self_exclusion>`_
    