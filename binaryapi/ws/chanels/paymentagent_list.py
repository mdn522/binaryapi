"""Module for Binary paymentagent_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#paymentagent_list

class PaymentagentList(Base):
    """Class for Binary paymentagent_list websocket chanel."""

    name = "paymentagent_list"

    def __call__(self, paymentagent_list: str, currency: str=None, passthrough=None, req_id: int=None):
        """Method to send message to paymentagent_list websocket chanel.
        Payment Agent: List (request)
        Will return a list of Payment Agents for a given country for a given currency. Payment agents allow users to deposit and withdraw funds using local payment methods that might not be available via the main website's cashier system.
        :param paymentagent_list: Client's 2-letter country code (obtained from `residence_list` call).
        :type paymentagent_list: str
        :param currency: [Optional] If specified, only payment agents that supports that currency will be returned (obtained from `payout_currencies` call).
        :type currency: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "paymentagent_list": paymentagent_list
        }

        if currency:
            data['currency'] = currency

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
