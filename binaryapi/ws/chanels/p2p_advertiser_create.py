"""Module for Binary p2p_advertiser_create websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#p2p_advertiser_create

class P2PAdvertiserCreate(Base):
    """Class for Binary p2p_advertiser_create websocket channel."""

    name = "p2p_advertiser_create"

    def __call__(
        self, 
        name: str, 
        contact_info: Optional[str] = None, 
        default_advert_description: Optional[str] = None, 
        payment_info: Optional[str] = None, 
        subscribe: Optional[Union[bool, int]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advertiser_create websocket channel.
        P2P Advertiser Create (request)
        Registers the client as a P2P advertiser.

        :param name: The advertiser's displayed name.
        :type name: str
        :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
        :type contact_info: Optional[str]
        :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
        :type default_advert_description: Optional[str]
        :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
        :type payment_info: Optional[str]
        :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to advertiser
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advertiser_create": int(1),
            "name": name
        }

        if contact_info:
            data['contact_info'] = str(contact_info)

        if default_advert_description:
            data['default_advert_description'] = str(default_advert_description)

        if payment_info:
            data['payment_info'] = str(payment_info)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
