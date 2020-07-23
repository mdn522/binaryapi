"""Module for Binary reality_check websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#reality_check

class RealityCheck(Base):
    """Class for Binary reality_check websocket chanel."""

    name = "reality_check"

    def __call__(self, passthrough=None, req_id: int = None):
        """Method to send message to reality_check websocket chanel.
        Reality Check (request)
        Retrieve summary of client's trades and account for the Reality Check facility. A 'reality check' means a display of time elapsed since the session began, and associated client profit/loss. The Reality Check facility is a regulatory requirement for certain landing companies.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "reality_check": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
