"""Module for Binary trading_servers websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#trading_servers

class TradingServers(Base):
    """Class for Binary trading_servers websocket channel."""

    name = "trading_servers"

    def __call__(self, account_type: Optional[str] = None, environment: Optional[str] = None, market_type: Optional[str] = None, platform: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to trading_servers websocket channel.
        Server list (request)
        Get the list of servers for platform. Currently, only mt5 is supported
        :param account_type: [Optional] Trading account type.
        :type account_type: Optional[str]
        :param environment: [Optional] Pass the environment (installation) instance. Currently, there are one demo and two real environments. Defaults to 'all'.
        :type environment: Optional[str]
        :param market_type: [Optional] Market type.
        :type market_type: Optional[str]
        :param platform: [Optional] Pass the trading platform name, default to mt5
        :type platform: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "trading_servers": int(1)
        }

        if account_type:
            data['account_type'] = str(account_type)

        if environment:
            data['environment'] = str(environment)

        if market_type:
            data['market_type'] = str(market_type)

        if platform:
            data['platform'] = str(platform)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
