"""Module for Binary p2p_order_create websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_order_create

class P2POrderCreate(Base):
    """Class for Binary p2p_order_create websocket chanel."""

    name = "p2p_order_create"

    def __call__(self, advert_id: str, amount, contact_info: str = None, payment_info: str = None, subscribe: bool = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_order_create websocket chanel.
        P2P Order Create (request)
        Creates a P2P order for the specified advert. **This API call is still in Beta.**
        :param advert_id: The unique identifier for the advert to create an order against.
        :type advert_id: str
        :param amount: The amount of currency to be bought or sold.
        :type amount: 
        :param contact_info: [Optional] Seller contact information. Only applicable for 'sell orders'.
        :type contact_info: str
        :param payment_info: [Optional] Payment instructions. Only applicable for 'sell orders'.
        :type payment_info: str
        :param subscribe: [Optional] If set to 1, will send updates whenever there is an update to the order.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_order_create": 1,
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
