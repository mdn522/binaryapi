"""Module for Binary p2p_order_list websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#p2p_order_list

class P2POrderList(Base):
    """Class for Binary p2p_order_list websocket channel."""

    name = "p2p_order_list"

    def __call__(
        self, 
        active: Optional[Union[int, float, Decimal]] = None, 
        advert_id: Optional[str] = None, 
        limit: Optional[int] = None, 
        offset: Optional[int] = None, 
        subscribe: Optional[Union[bool, int]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_order_list websocket channel.
        P2P Order List (request)
        List active orders.

        :param active: [Optional] Should be 1 to list active, 0 to list inactive (historical).
        :type active: Optional[Union[int, float, Decimal]]
        :param advert_id: [Optional] If present, lists orders applying to a specific advert.
        :type advert_id: Optional[str]
        :param limit: [Optional] Used for paging.
        :type limit: Optional[int]
        :param offset: [Optional] Used for paging.
        :type offset: Optional[int]
        :param subscribe: [Optional] If set to 1, will send updates whenever there is a change to any order belonging to you.
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_order_list": int(1)
        }

        if active:
            data['active'] = active

        if advert_id:
            data['advert_id'] = str(advert_id)

        if limit:
            data['limit'] = int(limit)

        if offset:
            data['offset'] = int(offset)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
