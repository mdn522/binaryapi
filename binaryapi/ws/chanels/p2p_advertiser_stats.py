"""Module for Binary p2p_advertiser_stats websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_advertiser_stats

class P2PAdvertiserStats(Base):
    """Class for Binary p2p_advertiser_stats websocket channel."""

    name = "p2p_advertiser_stats"

    def __call__(self, days: Optional[int] = None, id: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_advertiser_stats websocket channel.
        P2P Advertiser Statistics (request)
        Retrieve historical trade statistics of a P2P advertiser. **This API call is still in Beta.**
        :param days: [Optional] The time period to create statistics for, in days. If not provided, 30 days will be used.
        :type days: Optional[int]
        :param id: [Optional] The unique identifier for this advertiser. If not provided, returns advertiser statistics of the current account.
        :type id: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_advertiser_stats": int(1)
        }

        if days:
            data['days'] = int(days)

        if id:
            data['id'] = str(id)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
