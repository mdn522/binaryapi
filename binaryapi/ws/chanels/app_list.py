"""Module for Binary app_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#app_list

class AppList(Base):
    """Class for Binary app_list websocket chanel."""

    name = "app_list"

    def __call__(self, passthrough=None, req_id: int=None):
        """Method to send message to app_list websocket chanel.
        Application: List (request)
        List all of the account's OAuth applications
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "app_list": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
