"""Module for Binary exchange_rates websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#exchange_rates

class ExchangeRates(Base):
    """Class for Binary exchange_rates websocket channel."""

    name = "exchange_rates"

    def __call__(self, base_currency: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to exchange_rates websocket channel.
        Exchange Rates (request)
        Retrieves the exchange rates from a base currency to all currencies supported by the system.
        :param base_currency: Base currency (can be obtained from `payout_currencies` call)
        :type base_currency: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "exchange_rates": int(1),
            "base_currency": base_currency
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
