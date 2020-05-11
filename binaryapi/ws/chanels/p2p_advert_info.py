"""Module for Binary p2p_advert_info websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advert_info

class P2PAdvertInfo(Base):
    """Class for Binary p2p_advert_info websocket chanel."""

    name = "p2p_advert_info"

    def __call__(self, id: str, passthrough=None, req_id: int = None):
        """Method to send message to p2p_advert_info websocket chanel.
        P2P Advert Information (request)
        Retrieve information about a P2P advert. **This API call is still in Beta.**
        :param id: The unique identifier for this advert.
        :type id: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advert_info": 1,
            "id": id
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
