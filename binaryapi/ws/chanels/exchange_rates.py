"""Module for Binary exchange_rates websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#exchange_rates

class ExchangeRates(Base):
    """Class for Binary exchange_rates websocket chanel."""

    name = "exchange_rates"

    def __call__(self, base_currency: str, passthrough=None, req_id: int=None):
        """Method to send message to exchange_rates websocket chanel.
        Exchange Rates (request)
        Retrieves the exchange rates from a base currency to all currencies supported by the system.
        :param base_currency: Base currency (can be obtained from `payout_currencies` call)
        :type base_currency: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "exchange_rates": 1,
            "base_currency": base_currency
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
