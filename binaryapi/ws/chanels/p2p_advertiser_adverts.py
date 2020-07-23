"""Module for Binary p2p_advertiser_adverts websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advertiser_adverts

class P2PAdvertiserAdverts(Base):
    """Class for Binary p2p_advertiser_adverts websocket chanel."""

    name = "p2p_advertiser_adverts"

    def __call__(self, limit: int = None, offset: int = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_advertiser_adverts websocket chanel.
        P2P Advertiser Adverts (request)
        Returns all P2P adverts created by the authorized client. Can only be used by a registered P2P advertiser. **This API call is still in Beta.**
        :param limit: [Optional] Used for paging.
        :type limit: int
        :param offset: [Optional] Used for paging.
        :type offset: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advertiser_adverts": int(1)
        }

        if limit:
            data['limit'] = int(limit)

        if offset:
            data['offset'] = int(offset)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
