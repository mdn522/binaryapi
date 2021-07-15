"""Module for Binary p2p_advert_info websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#p2p_advert_info

class P2PAdvertInfo(Base):
    """Class for Binary p2p_advert_info websocket channel."""

    name = "p2p_advert_info"

    def __call__(self, id: str, use_client_limits: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_advert_info websocket channel.
        P2P Advert Information (request)
        Retrieve information about a P2P advert. **This API call is still in Beta.**
        :param id: The unique identifier for this advert.
        :type id: str
        :param use_client_limits: [Optional] If set to 1, the maximum order amount will be adjusted to the current balance and turnover limits of the account.
        :type use_client_limits: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_advert_info": int(1),
            "id": id
        }

        if use_client_limits:
            data['use_client_limits'] = int(use_client_limits)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
