"""Module for Binary residence_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#residence_list

class ResidenceList(Base):
    """Class for Binary residence_list websocket chanel."""

    name = "residence_list"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to residence_list websocket chanel.
        Countries List (request)
        This call returns a list of countries and 2-letter country codes, suitable for populating the account opening form.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "residence_list": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
