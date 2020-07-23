"""Module for Binary p2p_advertiser_info websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advertiser_info

class P2PAdvertiserInfo(Base):
    """Class for Binary p2p_advertiser_info websocket chanel."""

    name = "p2p_advertiser_info"

    def __call__(self, id: str = None, subscribe: bool = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_advertiser_info websocket chanel.
        P2P Advertiser Information (request)
        Retrieve information about a P2P advertiser. **This API call is still in Beta.**
        :param id: [Optional] The unique identifier for this advertiser. If not provided, returns advertiser information about the current account.
        :type id: str
        :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to advertiser
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advertiser_info": int(1)
        }

        if id:
            data['id'] = str(id)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
