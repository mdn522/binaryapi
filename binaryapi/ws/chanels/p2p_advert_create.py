"""Module for Binary p2p_advert_create websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional, Union
from decimal import Decimal


# https://developers.binary.com/api/#p2p_advert_create

class P2PAdvertCreate(Base):
    """Class for Binary p2p_advert_create websocket channel."""

    name = "p2p_advert_create"

    def __call__(
        self, 
        amount: Union[int, float, Decimal], 
        max_order_amount: Union[int, float, Decimal], 
        min_order_amount: Union[int, float, Decimal], 
        rate: Union[int, float, Decimal], 
        type: str, 
        contact_info: Optional[str] = None, 
        description: Optional[str] = None, 
        local_currency: Optional[str] = None, 
        payment_info: Optional[str] = None, 
        payment_method: Optional[str] = None, 
        payment_method_ids: Optional[List] = None, 
        payment_method_names: Optional[List] = None, 
        rate_type: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advert_create websocket channel.
        P2P Advert Create (request)
        Creates a P2P (Peer to Peer) advert. Can only be used by an approved P2P advertiser.

        :param amount: The total amount of the advert, in advertiser's account currency.
        :type amount: Union[int, float, Decimal]
        :param max_order_amount: Maximum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be more than or equal to `min_order_amount`
        :type max_order_amount: Union[int, float, Decimal]
        :param min_order_amount: Minimum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be less than or equal to `max_order_amount`.
        :type min_order_amount: Union[int, float, Decimal]
        :param rate: Conversion rate from advertiser's account currency to `local_currency`. An absolute rate value (fixed), or percentage offset from current market rate (floating).
        :type rate: Union[int, float, Decimal]
        :param type: The advertisement represents the intention to perform this action on your Deriv account funds.
        :type type: str
        :param contact_info: [Optional] Advertiser contact information.
        :type contact_info: Optional[str]
        :param description: [Optional] General information about the advert.
        :type description: Optional[str]
        :param local_currency: [Optional] Local currency for this advert. If not provided, will use the currency of client's residence by default.
        :type local_currency: Optional[str]
        :param payment_info: [Optional] Payment instructions.
        :type payment_info: Optional[str]
        :param payment_method: [Optional] Payment method name (deprecated).
        :type payment_method: Optional[str]
        :param payment_method_ids: IDs of previously saved payment methods as returned from p2p_advertiser_payment_methods, only applicable for sell ads.
        :type payment_method_ids: Optional[List]
        :param payment_method_names: Payment method identifiers as returned from p2p_payment_methods, only applicable for buy ads.
        :type payment_method_names: Optional[List]
        :param rate_type: Type of rate, fixed or floating.
        :type rate_type: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advert_create": int(1),
            "amount": amount,
            "max_order_amount": max_order_amount,
            "min_order_amount": min_order_amount,
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

        if payment_method:
            data['payment_method'] = str(payment_method)

        if payment_method_ids:
            data['payment_method_ids'] = payment_method_ids

        if payment_method_names:
            data['payment_method_names'] = payment_method_names

        if rate_type:
            data['rate_type'] = str(rate_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
