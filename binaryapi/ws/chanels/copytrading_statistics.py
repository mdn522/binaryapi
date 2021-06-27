"""Module for Binary copytrading_statistics websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#copytrading_statistics

class CopytradingStatistics(Base):
    """Class for Binary copytrading_statistics websocket channel."""

    name = "copytrading_statistics"

    def __call__(self, trader_id: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to copytrading_statistics websocket channel.
        Copy Trading: Statistics (request)
        Retrieve performance, trading, risk and copiers statistics of trader.
        :param trader_id: The ID of the target trader.
        :type trader_id: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "copytrading_statistics": int(1),
            "trader_id": trader_id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
