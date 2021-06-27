"""Module for Binary tnc_approval websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Optional, Union, Any


# https://developers.binary.com/api/#tnc_approval

class TncApproval(Base):
    """Class for Binary tnc_approval websocket channel."""

    name = "tnc_approval"

    def __call__(self, ukgc_funds_protection: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to tnc_approval websocket channel.
        Terms and Conditions Approval (request)
        To approve the latest version of terms and conditions.
        :param ukgc_funds_protection: [Optional] For `ASK_UK_FUNDS_PROTECTION` in `cashier`.
        :type ukgc_funds_protection: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "tnc_approval": 1
        }

        if ukgc_funds_protection:
            data['ukgc_funds_protection'] = int(ukgc_funds_protection)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
