"""Module for Binary set_self_exclusion websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#set_self_exclusion

class SetSelfExclusion(Base):
    """Class for Binary set_self_exclusion websocket channel."""

    name = "set_self_exclusion"

    def __call__(
        self, 
        exclude_until: Optional[str] = None, 
        max_30day_deposit: Optional[Union[int, float, Decimal]] = None, 
        max_30day_losses: Optional[Union[int, float, Decimal]] = None, 
        max_30day_turnover: Optional[Union[int, float, Decimal]] = None, 
        max_7day_deposit: Optional[Union[int, float, Decimal]] = None, 
        max_7day_losses: Optional[Union[int, float, Decimal]] = None, 
        max_7day_turnover: Optional[Union[int, float, Decimal]] = None, 
        max_balance: Optional[Union[int, float, Decimal]] = None, 
        max_deposit: Optional[Union[int, float, Decimal]] = None, 
        max_losses: Optional[Union[int, float, Decimal]] = None, 
        max_open_bets: Optional[int] = None, 
        max_turnover: Optional[Union[int, float, Decimal]] = None, 
        session_duration_limit: Optional[int] = None, 
        timeout_until: Optional[int] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to set_self_exclusion websocket channel.
        Set Self-Exclusion (request)
        Set Self-Exclusion (this call should be used in conjunction with `get_self_exclusion`)

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
        """

        data = {
            "set_self_exclusion": int(1)
        }

        if exclude_until:
            data['exclude_until'] = str(exclude_until)

        if max_30day_deposit:
            data['max_30day_deposit'] = max_30day_deposit

        if max_30day_losses:
            data['max_30day_losses'] = max_30day_losses

        if max_30day_turnover:
            data['max_30day_turnover'] = max_30day_turnover

        if max_7day_deposit:
            data['max_7day_deposit'] = max_7day_deposit

        if max_7day_losses:
            data['max_7day_losses'] = max_7day_losses

        if max_7day_turnover:
            data['max_7day_turnover'] = max_7day_turnover

        if max_balance:
            data['max_balance'] = max_balance

        if max_deposit:
            data['max_deposit'] = max_deposit

        if max_losses:
            data['max_losses'] = max_losses

        if max_open_bets:
            data['max_open_bets'] = int(max_open_bets)

        if max_turnover:
            data['max_turnover'] = max_turnover

        if session_duration_limit:
            data['session_duration_limit'] = int(session_duration_limit)

        if timeout_until:
            data['timeout_until'] = int(timeout_until)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
