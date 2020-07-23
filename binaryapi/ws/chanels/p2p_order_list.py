"""Module for Binary p2p_order_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_order_list

class P2POrderList(Base):
    """Class for Binary p2p_order_list websocket chanel."""

    name = "p2p_order_list"

    def __call__(self, active=None, advert_id: str = None, limit: int = None, offset: int = None, subscribe: bool = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_order_list websocket chanel.
        P2P Order List (request)
        List active orders. **This API call is still in Beta.**
        :param active: [Optional] Should be 1 to list active, 0 to list inactive (historical).
        :type active: 
        :param advert_id: [Optional] If present, lists orders applying to a specific advert.
        :type advert_id: str
        :param limit: [Optional] Used for paging.
        :type limit: int
        :param offset: [Optional] Used for paging.
        :type offset: int
        :param subscribe: [Optional] If set to 1, will send updates whenever there is a change to any order belonging to you.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
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
