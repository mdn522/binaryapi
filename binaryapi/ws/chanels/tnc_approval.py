"""Module for Binary tnc_approval websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#tnc_approval

class TncApproval(Base):
    """Class for Binary tnc_approval websocket channel."""

    name = "tnc_approval"

    def __call__(
        self, 
        affiliate_coc_agreement: Optional[int] = None, 
        ukgc_funds_protection: Optional[int] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to tnc_approval websocket channel.
        Terms and Conditions Approval (request)
        To approve the latest version of terms and conditions.

        :param affiliate_coc_agreement: [Optional] For Affiliate's Code of Conduct Agreement.
        :type affiliate_coc_agreement: Optional[int]
        :param ukgc_funds_protection: [Optional] For `ASK_UK_FUNDS_PROTECTION` in `cashier`.
        :type ukgc_funds_protection: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "tnc_approval": 1
        }

        if affiliate_coc_agreement:
            data['affiliate_coc_agreement'] = int(affiliate_coc_agreement)

        if ukgc_funds_protection:
            data['ukgc_funds_protection'] = int(ukgc_funds_protection)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
