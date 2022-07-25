"""Module for Binary p2p_advertiser_payment_methods websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional


# https://developers.binary.com/api/#p2p_advertiser_payment_methods

class P2PAdvertiserPaymentMethods(Base):
    """Class for Binary p2p_advertiser_payment_methods websocket channel."""

    name = "p2p_advertiser_payment_methods"

    def __call__(
        self, 
        create: Optional[List] = None, 
        delete: Optional[List] = None, 
        update=None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to p2p_advertiser_payment_methods websocket channel.
        P2P Advertiser Payment Methods (request)
        Manage or list P2P advertiser payment methods.

        :param create: Contains new payment method entries.
        :type create: Optional[List]
        :param delete: Contains payment methods to delete.
        :type delete: Optional[List]
        :param update: Contains payment methods to update.
        :type update: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "p2p_advertiser_payment_methods": int(1)
        }

        if create:
            data['create'] = create

        if delete:
            data['delete'] = delete

        if update:
            data['update'] = update

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
