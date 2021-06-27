"""Module for Binary p2p_order_create websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Union, Optional, Any
from decimal import Decimal


# https://developers.binary.com/api/#p2p_order_create

class P2POrderCreate(Base):
    """Class for Binary p2p_order_create websocket channel."""

    name = "p2p_order_create"

    def __call__(self, advert_id: str, amount: Union[int, float, Decimal], contact_info: Optional[str] = None, payment_info: Optional[str] = None, subscribe: Union[bool, int, None] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_order_create websocket channel.
        P2P Order Create (request)
        Creates a P2P order for the specified advert. **This API call is still in Beta.**
        :param advert_id: The unique identifier for the advert to create an order against.
        :type advert_id: str
        :param amount: The amount of currency to be bought or sold.
        :type amount: Union[int, float, Decimal]
        :param contact_info: [Optional] Seller contact information. Only applicable for 'sell orders'.
        :type contact_info: Optional[str]
        :param payment_info: [Optional] Payment instructions. Only applicable for 'sell orders'.
        :type payment_info: Optional[str]
        :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to the order.
        :type subscribe: Union[bool, int, None]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_order_create": int(1),
            "advert_id": advert_id,
            "amount": amount
        }

        if contact_info:
            data['contact_info'] = str(contact_info)

        if payment_info:
            data['payment_info'] = str(payment_info)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
