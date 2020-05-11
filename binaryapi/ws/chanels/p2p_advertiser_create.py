"""Module for Binary p2p_advertiser_create websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advertiser_create

class P2PAdvertiserCreate(Base):
    """Class for Binary p2p_advertiser_create websocket chanel."""

    name = "p2p_advertiser_create"

    def __call__(self, name: str, contact_info: str=None, default_advert_description: str=None, payment_info: str=None, subscribe: bool=None, passthrough=None, req_id: int=None):
        """Method to send message to p2p_advertiser_create websocket chanel.
        P2P Advertiser Create (request)
        Registers the client as a P2P advertiser. **This API call is still in Beta.**
        :param name: The advertiser's displayed name.
        :type name: str
        :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
        :type contact_info: str
        :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
        :type default_advert_description: str
        :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
        :type payment_info: str
        :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to advertiser
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advertiser_create": 1,
            "name": name
        }

        if contact_info:
            data['contact_info'] = contact_info

        if default_advert_description:
            data['default_advert_description'] = default_advert_description

        if payment_info:
            data['payment_info'] = payment_info

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
