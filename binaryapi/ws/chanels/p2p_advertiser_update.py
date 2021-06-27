"""Module for Binary p2p_advertiser_update websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#p2p_advertiser_update

class P2PAdvertiserUpdate(Base):
    """Class for Binary p2p_advertiser_update websocket channel."""

    name = "p2p_advertiser_update"

    def __call__(self, contact_info: Optional[str] = None, default_advert_description: Optional[str] = None, is_listed: Optional[int] = None, payment_info: Optional[str] = None, show_name: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_advertiser_update websocket channel.
        P2P Advertiser Update (request)
        Update the information of the P2P advertiser for the current account. Can only be used by an approved P2P advertiser. **This API call is still in Beta.**
        :param contact_info: [Optional] Advertiser's contact information, to be used as a default for new sell adverts.
        :type contact_info: Optional[str]
        :param default_advert_description: [Optional] Default description that can be used every time an advert is created.
        :type default_advert_description: Optional[str]
        :param is_listed: [Optional] Used to set if the advertiser's adverts could be listed. When `0`, adverts won't be listed regardless of they are active or not. This doesn't change the `is_active` of each individual advert.
        :type is_listed: Optional[int]
        :param payment_info: [Optional] Advertiser's payment information, to be used as a default for new sell adverts.
        :type payment_info: Optional[str]
        :param show_name: [Optional] When `1`, the advertiser's real name will be displayed on to other users on adverts and orders.
        :type show_name: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_advertiser_update": int(1)
        }

        if contact_info:
            data['contact_info'] = str(contact_info)

        if default_advert_description:
            data['default_advert_description'] = str(default_advert_description)

        if is_listed:
            data['is_listed'] = int(is_listed)

        if payment_info:
            data['payment_info'] = str(payment_info)

        if show_name:
            data['show_name'] = int(show_name)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
