"""Module for Binary p2p_advert_create websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advert_create

class P2PAdvertCreate(Base):
    """Class for Binary p2p_advert_create websocket chanel."""

    name = "p2p_advert_create"

    def __call__(self, amount, max_order_amount, min_order_amount, payment_method: str, rate, type: str, contact_info: str = None, description: str = None, local_currency: str = None, payment_info: str = None, passthrough=None, req_id: int = None):
        """Method to send message to p2p_advert_create websocket chanel.
        P2P Advert Create (request)
        Creates a P2P (Peer to Peer) advert. Can only be used by an approved P2P advertiser. **This API call is still in Beta.**
        :param amount: The total amount of the advert, in advertiser's account currency.
        :type amount: 
        :param max_order_amount: Maximum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be less than or equal to total `amount` of the advert.
        :type max_order_amount: 
        :param min_order_amount: Minimum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be less than `max_order_amount`.
        :type min_order_amount: 
        :param payment_method: The payment method.
        :type payment_method: str
        :param rate: Conversion rate from advertiser's account currency to `local_currency`.
        :type rate: 
        :param type: Whether this is a buy or a sell.
        :type type: str
        :param contact_info: [Optional] Advertiser contact information. Only applicable for 'sell adverts'.
        :type contact_info: str
        :param description: [Optional] General information about the advert.
        :type description: str
        :param local_currency: [Optional] Local currency for this advert. If not provided, will use the currency of client's residence by default.
        :type local_currency: str
        :param payment_info: [Optional] Payment instructions. Only applicable for 'sell adverts'.
        :type payment_info: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advert_create": int(1),
            "amount": amount,
            "max_order_amount": max_order_amount,
            "min_order_amount": min_order_amount,
            "payment_method": payment_method,
            "rate": rate,
            "type": type
        }

        if contact_info:
            data['contact_info'] = str(contact_info)

        if description:
            data['description'] = str(description)

        if local_currency:
            data['local_currency'] = str(local_currency)

        if payment_info:
            data['payment_info'] = str(payment_info)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
