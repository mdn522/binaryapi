"""Module for Binary set_self_exclusion websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#set_self_exclusion

class SetSelfExclusion(Base):
    """Class for Binary set_self_exclusion websocket chanel."""

    name = "set_self_exclusion"

    def __call__(self, exclude_until=None, max_30day_losses=None, max_30day_turnover=None, max_7day_losses=None, max_7day_turnover=None, max_balance=None, max_deposit=None, max_deposit_end_date=None, max_losses=None, max_open_bets=None, max_turnover=None, session_duration_limit=None, timeout_until=None, passthrough=None, req_id: int = None):
        """Method to send message to set_self_exclusion websocket chanel.
        Set Self-Exclusion (request)
        Set Self-Exclusion (this call should be used in conjunction with `get_self_exclusion`)
        :param exclude_until: [Optional] Exclude me from the website (for a minimum of 6 months, up to a maximum of 5 years). Note: uplifting this self-exclusion may require contacting the company.
        :type exclude_until: 
        :param max_30day_losses: [Optional] 30-day limit on losses.
        :type max_30day_losses: 
        :param max_30day_turnover: [Optional] 30-day turnover limit.
        :type max_30day_turnover: 
        :param max_7day_losses: [Optional] 7-day limit on losses.
        :type max_7day_losses: 
        :param max_7day_turnover: [Optional] 7-day turnover limit.
        :type max_7day_turnover: 
        :param max_balance: [Optional] Maximum account cash balance.
        :type max_balance: 
        :param max_deposit: [Optional] Deposit limit.
        :type max_deposit: 
        :param max_deposit_end_date: [Optional] Exclude me from making deposits when the cumulative sum of deposits exceeds specified deposit limit.
        :type max_deposit_end_date: 
        :param max_losses: [Optional] Daily limit on losses.
        :type max_losses: 
        :param max_open_bets: [Optional] Maximum number of open positions.
        :type max_open_bets: 
        :param max_turnover: [Optional] Daily turnover limit.
        :type max_turnover: 
        :param session_duration_limit: [Optional] Session duration limit, in minutes.
        :type session_duration_limit: 
        :param timeout_until: [Optional] Exclude me from the website (for up to 6 weeks). Requires time in epoch format. Note: unlike `exclude_until`, this self-exclusion will be lifted automatically at the expiry of the timeout period.
        :type timeout_until: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "set_self_exclusion": int(1)
        }

        if exclude_until:
            data['exclude_until'] = exclude_until

        if max_30day_losses:
            data['max_30day_losses'] = max_30day_losses

        if max_30day_turnover:
            data['max_30day_turnover'] = max_30day_turnover

        if max_7day_losses:
            data['max_7day_losses'] = max_7day_losses

        if max_7day_turnover:
            data['max_7day_turnover'] = max_7day_turnover

        if max_balance:
            data['max_balance'] = max_balance

        if max_deposit:
            data['max_deposit'] = max_deposit

        if max_deposit_end_date:
            data['max_deposit_end_date'] = max_deposit_end_date

        if max_losses:
            data['max_losses'] = max_losses

        if max_open_bets:
            data['max_open_bets'] = max_open_bets

        if max_turnover:
            data['max_turnover'] = max_turnover

        if session_duration_limit:
            data['session_duration_limit'] = session_duration_limit

        if timeout_until:
            data['timeout_until'] = timeout_until

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
