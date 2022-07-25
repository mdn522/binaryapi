"""Module for Binary p2p_advertiser_adverts websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_advertiser_adverts

class P2PAdvertiserAdverts(Base):
    """Class for Binary p2p_advertiser_adverts websocket channel."""

    name = "p2p_advertiser_adverts"

    def __call__(
        self, 
        limit: Optional[int] = None, 
        offset: Optional[int] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advertiser_adverts websocket channel.
        P2P Advertiser Adverts (request)
        Returns all P2P adverts created by the authorized client. Can only be used by a registered P2P advertiser.

        :param limit: [Optional] Used for paging. This value will also apply to subsription responses.
        :type limit: Optional[int]
        :param offset: [Optional] Used for paging. This value will also apply to subsription responses.
        :type offset: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advertiser_adverts": int(1)
        }

        if limit:
            data['limit'] = int(limit)

        if offset:
            data['offset'] = int(offset)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
