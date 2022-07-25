"""Module for Binary p2p_advertiser_relations websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional


# https://developers.binary.com/api/#p2p_advertiser_relations

class P2PAdvertiserRelations(Base):
    """Class for Binary p2p_advertiser_relations websocket channel."""

    name = "p2p_advertiser_relations"

    def __call__(
        self, 
        add_blocked: Optional[List] = None, 
        add_favourites: Optional[List] = None, 
        remove_blocked: Optional[List] = None, 
        remove_favourites: Optional[List] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advertiser_relations websocket channel.
        P2P Advertiser Relations (request)
        Updates and returns favourite and blocked advertisers of the current user.

        :param add_blocked: IDs of advertisers to block.
        :type add_blocked: Optional[List]
        :param add_favourites: IDs of advertisers to add as favourites.
        :type add_favourites: Optional[List]
        :param remove_blocked: IDs of advertisers to remove from blocked.
        :type remove_blocked: Optional[List]
        :param remove_favourites: IDs of advertisers to remove from favourites.
        :type remove_favourites: Optional[List]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advertiser_relations": int(1)
        }

        if add_blocked:
            data['add_blocked'] = add_blocked

        if add_favourites:
            data['add_favourites'] = add_favourites

        if remove_blocked:
            data['remove_blocked'] = remove_blocked

        if remove_favourites:
            data['remove_favourites'] = remove_favourites

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
