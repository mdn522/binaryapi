"""Module for Binary crypto_config websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#crypto_config

class CryptoConfig(Base):
    """Class for Binary crypto_config websocket channel."""

    name = "crypto_config"

    def __call__(
        self, 
        currency_code: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to crypto_config websocket channel.
        Cryptocurrency configurations (request)
        The request for cryptocurrencies configuration.

        :param currency_code: [Optional] Cryptocurrency code. Sending request with currency_code provides crypto config for the sent cryptocurrency code only.
        :type currency_code: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "crypto_config": int(1)
        }

        if currency_code:
            data['currency_code'] = str(currency_code)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
