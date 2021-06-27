"""Module for Binary p2p_advert_update websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any, List


# https://developers.binary.com/api/#p2p_advert_update

class P2PAdvertUpdate(Base):
    """Class for Binary p2p_advert_update websocket channel."""

    name = "p2p_advert_update"

    def __call__(self, id: str, delete: Optional[int] = None, is_active: Optional[int] = None, payment_method: Optional[str] = None, payment_method_ids: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_advert_update websocket channel.
        P2P Advert Update (request)
        Updates a P2P advert. Can only be used by the advertiser. **This API call is still in Beta.**
        :param id: The unique identifier for this advert.
        :type id: str
        :param delete: [Optional] If set to 1, permanently deletes the advert.
        :type delete: Optional[int]
        :param is_active: [Optional] Activate or deactivate the advert.
        :type is_active: Optional[int]
        :param payment_method: [Optional] Supported payment methods. Separate multiple values with a comma, maximum 3.
        :type payment_method: Optional[str]
        :param payment_method_ids: [Optional] IDs of payment methods, only applicable for sell ads. Will replace exisiting methods.
        :type payment_method_ids: Optional[List]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_advert_update": int(1),
            "id": id
        }

        if delete:
            data['delete'] = int(delete)

        if is_active:
            data['is_active'] = int(is_active)

        if payment_method:
            data['payment_method'] = str(payment_method)

        if payment_method_ids:
            data['payment_method_ids'] = payment_method_ids

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
