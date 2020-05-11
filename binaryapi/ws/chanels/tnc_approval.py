"""Module for Binary tnc_approval websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#tnc_approval

class TncApproval(Base):
    """Class for Binary tnc_approval websocket chanel."""

    name = "tnc_approval"

    def __call__(self, ukgc_funds_protection: int = None, passthrough=None, req_id: int = None):
        """Method to send message to tnc_approval websocket chanel.
        Terms and Conditions Approval (request)
        To approve the latest version of terms and conditions.
        :param ukgc_funds_protection: [Optional] For `ASK_UK_FUNDS_PROTECTION` in `cashier`.
        :type ukgc_funds_protection: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "tnc_approval": 1
        }

        if ukgc_funds_protection:
            data['ukgc_funds_protection'] = int(ukgc_funds_protection)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
