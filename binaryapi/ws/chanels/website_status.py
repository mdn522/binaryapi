"""Module for Binary website_status websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#website_status

class WebsiteStatus(Base):
    """Class for Binary website_status websocket chanel."""

    name = "website_status"

    def __call__(self, subscribe: bool=None, passthrough=None, req_id: int=None):
        """Method to send message to website_status websocket chanel.
        Server Status (request)
        Request server status.
        :param subscribe: [Optional] `1` to stream the server/website status updates.
        :type subscribe: bool
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "website_status": 1
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
