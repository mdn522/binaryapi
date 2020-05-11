"""Module for Binary app_get websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#app_get

class AppGet(Base):
    """Class for Binary app_get websocket chanel."""

    name = "app_get"

    def __call__(self, app_get: int, passthrough=None, req_id: int = None):
        """Method to send message to app_get websocket chanel.
        Application: Get Details (request)
        To get the information of the OAuth application specified by 'app_id'
        :param app_get: Application app_id
        :type app_get: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "app_get": app_get
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
