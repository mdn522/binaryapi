"""Module for Binary exchange_rates websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#exchange_rates

class ExchangeRates(Base):
    """Class for Binary exchange_rates websocket channel."""

    name = "exchange_rates"

    def __call__(
        self, 
        base_currency: str, 
        subscribe: Optional[Union[bool, int]] = None, 
        target_currency: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to exchange_rates websocket channel.
        Exchange Rates (request)
        Retrieves the exchange rates from a base currency to all currencies supported by the system.

        :param base_currency: Base currency (can be obtained from `payout_currencies` call)
        :type base_currency: str
        :param subscribe: [Optional] 1 - to initiate a realtime stream of exchange rates relative to base currency.
        :type subscribe: Optional[Union[bool, int]]
        :param target_currency: [Optional] Local currency
        :type target_currency: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "exchange_rates": int(1),
            "base_currency": base_currency
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        if target_currency:
            data['target_currency'] = str(target_currency)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
