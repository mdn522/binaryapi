"""Module for Binary paymentagent_list websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#paymentagent_list

class PaymentagentList(Base):
    """Class for Binary paymentagent_list websocket channel."""

    name = "paymentagent_list"

    def __call__(
        self, 
        paymentagent_list: str, 
        currency: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to paymentagent_list websocket channel.
        Payment Agent: List (request)
        Will return a list of Payment Agents for a given country for a given currency. Payment agents allow users to deposit and withdraw funds using local payment methods that might not be available via the main website's cashier system.

        :param paymentagent_list: Client's 2-letter country code (obtained from `residence_list` call).
        :type paymentagent_list: str
        :param currency: [Optional] If specified, only payment agents that supports that currency will be returned (obtained from `payout_currencies` call).
        :type currency: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "paymentagent_list": paymentagent_list
        }

        if currency:
            data['currency'] = str(currency)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
