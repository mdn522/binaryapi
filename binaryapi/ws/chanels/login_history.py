"""Module for Binary login_history websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#login_history

class LoginHistory(Base):
    """Class for Binary login_history websocket chanel."""

    name = "login_history"

    def __call__(self, limit: int = None, passthrough=None, req_id: int = None):
        """Method to send message to login_history websocket chanel.
        Login History (request)
        Retrieve a summary of login history for user.
        :param limit: [Optional] Apply limit to count of login history records.
        :type limit: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "login_history": 1
        }

        if limit:
            data['limit'] = int(limit)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
