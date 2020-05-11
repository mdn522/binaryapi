"""Module for Binary states_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#states_list

class StatesList(Base):
    """Class for Binary states_list websocket chanel."""

    name = "states_list"

    def __call__(self, states_list: str, passthrough=None, req_id: int = None):
        """Method to send message to states_list websocket chanel.
        States List (request)
        For a given country, returns a list of States of that country. This is useful to populate the account opening form.
        :param states_list: Client's 2-letter country code (obtained from `residence_list` call)
        :type states_list: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "states_list": states_list
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
