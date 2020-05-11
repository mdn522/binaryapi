"""Module for Binary p2p_advert_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#p2p_advert_list

class P2PAdvertList(Base):
    """Class for Binary p2p_advert_list websocket chanel."""

    name = "p2p_advert_list"

    def __call__(self, advertiser_id: str=None, amount=None, counterparty_type: str=None, limit: int=None, local_currency: str=None, offset: int=None, passthrough=None, req_id: int=None):
        """Method to send message to p2p_advert_list websocket chanel.
        P2P Advert List (request)
        Returns available adverts for use with `p2p_order_create`. **This API call is still in Beta.**
        :param advertiser_id: [Optional] Which advertiser to list adverts for.
        :type advertiser_id: str
        :param amount: [Optional] How much to buy or sell, used to calculate prices.
        :type amount: 
        :param counterparty_type: [Optional] Filter the adverts by `counterparty_type`.
        :type counterparty_type: str
        :param limit: [Optional] Used for paging.
        :type limit: int
        :param local_currency: [Optional] Currency to conduct payment transaction in, defaults to the main currency for the client's country.
        :type local_currency: str
        :param offset: [Optional] Used for paging.
        :type offset: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "p2p_advert_list": 1
        }

        if advertiser_id:
            data['advertiser_id'] = advertiser_id

        if amount:
            data['amount'] = amount

        if counterparty_type:
            data['counterparty_type'] = counterparty_type

        if limit:
            data['limit'] = limit

        if local_currency:
            data['local_currency'] = local_currency

        if offset:
            data['offset'] = offset

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
