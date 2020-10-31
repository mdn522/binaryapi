"""Module for Binary landing_company websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#landing_company

class LandingCompany(Base):
    """Class for Binary landing_company websocket channel."""

    name = "landing_company"

    def __call__(self, landing_company: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to landing_company websocket channel.
        Landing Company (request)
        The company has a number of licensed subsidiaries in various jurisdictions, which are called Landing Companies. This call will return the appropriate Landing Company for clients of a given country. The landing company may differ for Gaming contracts (Synthetic Indices) and Financial contracts (Forex, Stock Indices, Commodities).
        :param landing_company: Client's 2-letter country code (obtained from `residence_list` call).
        :type landing_company: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "landing_company": landing_company
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
