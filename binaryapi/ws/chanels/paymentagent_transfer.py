"""Module for Binary paymentagent_transfer websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#paymentagent_transfer

class PaymentagentTransfer(Base):
    """Class for Binary paymentagent_transfer websocket channel."""

    name = "paymentagent_transfer"

    def __call__(
        self, 
        amount: Union[int, float, Decimal], 
        currency: str, 
        transfer_to: str, 
        description: Optional[str] = None, 
        dry_run: Optional[int] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to paymentagent_transfer websocket channel.
        Payment Agent: Transfer (request)
        Payment Agent Transfer - this call is available only to accounts that are approved Payment Agents.

        :param amount: The amount to transfer.
        :type amount: Union[int, float, Decimal]
        :param currency: Currency code.
        :type currency: str
        :param transfer_to: The loginid of the recipient account.
        :type transfer_to: str
        :param description: [Optional] Remarks about the transfer.
        :type description: Optional[str]
        :param dry_run: [Optional] If set to `1`, just do validation.
        :type dry_run: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "paymentagent_transfer": int(1),
            "amount": amount,
            "currency": currency,
            "transfer_to": transfer_to
        }

        if description:
            data['description'] = str(description)

        if dry_run:
            data['dry_run'] = int(dry_run)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
