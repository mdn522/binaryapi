"""Module for Binary p2p_advert_update websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional, Union
from decimal import Decimal


# https://developers.binary.com/api/#p2p_advert_update

class P2PAdvertUpdate(Base):
    """Class for Binary p2p_advert_update websocket channel."""

    name = "p2p_advert_update"

    def __call__(
        self, 
        id: str, 
        contact_info: Optional[str] = None, 
        delete: Optional[int] = None, 
        description: Optional[str] = None, 
        is_active: Optional[int] = None, 
        local_currency: Optional[str] = None, 
        max_order_amount: Optional[Union[int, float, Decimal]] = None, 
        min_order_amount: Optional[Union[int, float, Decimal]] = None, 
        payment_info: Optional[str] = None, 
        payment_method_ids: Optional[List] = None, 
        payment_method_names: Optional[List] = None, 
        rate: Optional[Union[int, float, Decimal]] = None, 
        rate_type: Optional[str] = None, 
        remaining_amount: Optional[Union[int, float, Decimal]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advert_update websocket channel.
        P2P Advert Update (request)
        Updates a P2P advert. Can only be used by the advertiser.

        :param id: The unique identifier for this advert.
        :type id: str
        :param contact_info: [Optional] Advertiser contact information.
        :type contact_info: Optional[str]
        :param delete: [Optional] If set to 1, permanently deletes the advert.
        :type delete: Optional[int]
        :param description: [Optional] General information about the advert.
        :type description: Optional[str]
        :param is_active: [Optional] Activate or deactivate the advert.
        :type is_active: Optional[int]
        :param local_currency: [Optional] Local currency for this advert.
        :type local_currency: Optional[str]
        :param max_order_amount: [Optional] Maximum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be more than or equal to `min_order_amount`.
        :type max_order_amount: Optional[Union[int, float, Decimal]]
        :param min_order_amount: [Optional] Minimum allowed amount for the orders of this advert, in advertiser's `account_currency`. Should be less than or equal to `max_order_amount`.
        :type min_order_amount: Optional[Union[int, float, Decimal]]
        :param payment_info: [Optional] Payment instructions.
        :type payment_info: Optional[str]
        :param payment_method_ids: [Optional] IDs of previously saved payment methods as returned from p2p_advertiser_payment_methods, only applicable for sell ads. Exisiting methods will be replaced.
        :type payment_method_ids: Optional[List]
        :param payment_method_names: [Optional] Payment method identifiers as returned from p2p_payment_methods, only applicable for buy ads. Exisiting methods will be replaced.
        :type payment_method_names: Optional[List]
        :param rate: [Optional] Conversion rate from advertiser's account currency to `local_currency`. An absolute rate value (fixed), or percentage offset from current market rate (floating).
        :type rate: Optional[Union[int, float, Decimal]]
        :param rate_type: [Optional] Type of rate, fixed or floating.
        :type rate_type: Optional[str]
        :param remaining_amount: [Optional] The total available amount of the advert, in advertiser's account currency.
        :type remaining_amount: Optional[Union[int, float, Decimal]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advert_update": int(1),
            "id": id
        }

        if contact_info:
            data['contact_info'] = str(contact_info)

        if delete:
            data['delete'] = int(delete)

        if description:
            data['description'] = str(description)

        if is_active:
            data['is_active'] = int(is_active)

        if local_currency:
            data['local_currency'] = str(local_currency)

        if max_order_amount:
            data['max_order_amount'] = max_order_amount

        if min_order_amount:
            data['min_order_amount'] = min_order_amount

        if payment_info:
            data['payment_info'] = str(payment_info)

        if payment_method_ids:
            data['payment_method_ids'] = payment_method_ids

        if payment_method_names:
            data['payment_method_names'] = payment_method_names

        if rate:
            data['rate'] = rate

        if rate_type:
            data['rate_type'] = str(rate_type)

        if remaining_amount:
            data['remaining_amount'] = remaining_amount

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
