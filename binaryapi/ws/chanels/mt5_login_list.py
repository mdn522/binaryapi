"""Module for Binary mt5_login_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#mt5_login_list

class Mt5LoginList(Base):
    """Class for Binary mt5_login_list websocket chanel."""

    name = "mt5_login_list"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to mt5_login_list websocket chanel.
        MT5: Accounts List (request)
        Get list of MT5 accounts for client
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "mt5_login_list": 1
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
