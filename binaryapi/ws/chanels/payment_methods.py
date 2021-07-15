"""Module for Binary payment_methods websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#payment_methods

class PaymentMethods(Base):
    """Class for Binary payment_methods websocket channel."""

    name = "payment_methods"

    def __call__(self, country: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to payment_methods websocket channel.
        Payment Methods (request)
        Will return a list payment methods available for the given country. If the request is authenticated the client's residence country will be used.
        :param country: [Optional] 2-letter country code (ISO standard).
        :type country: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "payment_methods": int(1)
        }

        if country:
            data['country'] = str(country)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
