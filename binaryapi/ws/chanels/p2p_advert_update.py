"""Module for Binary p2p_advert_update websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advert_update

class P2PAdvertUpdate(Base):
    """Class for Binary p2p_advert_update websocket chanel."""

    name = "p2p_advert_update"

    def __call__(self, id: str, delete: int = None, is_active: int = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_advert_update websocket chanel.
        P2P Advert Update (request)
        Updates a P2P advert. Can only be used by the advertiser. **This API call is still in Beta.**
        :param id: The unique identifier for this advert.
        :type id: str
        :param delete: [Optional] If set to 1, permanently deletes the advert.
        :type delete: int
        :param is_active: [Optional] Activate or deactivate the advert.
        :type is_active: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advert_update": int(1),
            "id": id
        }

        if delete:
            data['delete'] = int(delete)

        if is_active:
            data['is_active'] = int(is_active)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
