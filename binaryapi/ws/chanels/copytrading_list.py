"""Module for Binary copytrading_list websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#copytrading_list

class CopytradingList(Base):
    """Class for Binary copytrading_list websocket chanel."""

    name = "copytrading_list"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to copytrading_list websocket chanel.
        Copy Trading: List (request)
        Retrieves a list of active copiers and/or traders for Copy Trading
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "copytrading_list": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
