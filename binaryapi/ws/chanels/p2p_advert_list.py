"""Module for Binary p2p_advert_list websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Union, Optional, Any
from decimal import Decimal


# https://developers.binary.com/api/#p2p_advert_list

class P2PAdvertList(Base):
    """Class for Binary p2p_advert_list websocket channel."""

    name = "p2p_advert_list"

    def __call__(self, advertiser_id: Optional[str] = None, amount: Optional[Union[int, float, Decimal]] = None, counterparty_type: Optional[str] = None, limit: Optional[int] = None, local_currency: Optional[str] = None, offset: Optional[int] = None, use_client_limits: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to p2p_advert_list websocket channel.
        P2P Advert List (request)
        Returns available adverts for use with `p2p_order_create`. **This API call is still in Beta.**
        :param advertiser_id: [Optional] Which advertiser to list adverts for.
        :type advertiser_id: Optional[str]
        :param amount: [Optional] How much to buy or sell, used to calculate prices.
        :type amount: Optional[Union[int, float, Decimal]]
        :param counterparty_type: [Optional] Filter the adverts by `counterparty_type`.
        :type counterparty_type: Optional[str]
        :param limit: [Optional] Used for paging.
        :type limit: Optional[int]
        :param local_currency: [Optional] Currency to conduct payment transaction in, defaults to the main currency for the client's country.
        :type local_currency: Optional[str]
        :param offset: [Optional] Used for paging.
        :type offset: Optional[int]
        :param use_client_limits: [Optional] If set to 1, ads that exceed this account's balance or turnover limits will not be shown.
        :type use_client_limits: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "p2p_advert_list": int(1)
        }

        if advertiser_id:
            data['advertiser_id'] = str(advertiser_id)

        if amount:
            data['amount'] = amount

        if counterparty_type:
            data['counterparty_type'] = str(counterparty_type)

        if limit:
            data['limit'] = int(limit)

        if local_currency:
            data['local_currency'] = str(local_currency)

        if offset:
            data['offset'] = int(offset)

        if use_client_limits:
            data['use_client_limits'] = int(use_client_limits)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
