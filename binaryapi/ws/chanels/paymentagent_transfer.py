"""Module for Binary paymentagent_transfer websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#paymentagent_transfer

class PaymentagentTransfer(Base):
    """Class for Binary paymentagent_transfer websocket chanel."""

    name = "paymentagent_transfer"

    def __call__(self, amount, currency: str, transfer_to: str, description: str = None, dry_run: int = None, passthrough=None, req_id: int = None):
        """Method to send message to paymentagent_transfer websocket chanel.
        Payment Agent: Transfer (request)
        Payment Agent Transfer - this call is available only to accounts that are approved Payment Agents.
        :param amount: The amount to transfer.
        :type amount: 
        :param currency: Currency code.
        :type currency: str
        :param transfer_to: The loginid of the recipient account.
        :type transfer_to: str
        :param description: [Optional] Remarks about the transfer.
        :type description: str
        :param dry_run: [Optional] If set to `1`, just do validation.
        :type dry_run: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "paymentagent_transfer": 1,
            "amount": amount,
            "currency": currency,
            "transfer_to": transfer_to
        }

        if description:
            data['description'] = str(description)

        if dry_run:
            data['dry_run'] = int(dry_run)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
