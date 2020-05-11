"""Module for Binary get_account_status websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#get_account_status

class GetAccountStatus(Base):
    """Class for Binary get_account_status websocket chanel."""

    name = "get_account_status"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to get_account_status websocket chanel.
        Account Status (request)
        Get Account Status
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "get_account_status": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
