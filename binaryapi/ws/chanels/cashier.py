"""Module for Binary cashier websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Optional, Union


# https://developers.binary.com/api/#cashier

class Cashier(Base):
    """Class for Binary cashier websocket channel."""

    name = "cashier"

    def __call__(
        self, 
        cashier: str, 
        address: Optional[str] = None, 
        amount: Optional[Union[int, float, Decimal]] = None, 
        dry_run: Optional[int] = None, 
        provider: Optional[str] = None, 
        type: Optional[str] = None, 
        verification_code: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to cashier websocket channel.
        Cashier Information (request)
        Request the cashier info for the specified type.

        :param cashier: Operation which needs to be requested from cashier
        :type cashier: str
        :param address: [Optional] Address for crypto withdrawal. Only applicable for `api` type.
        :type address: Optional[str]
        :param amount: [Optional] Amount for crypto withdrawal. Only applicable for `api` type.
        :type amount: Optional[Union[int, float, Decimal]]
        :param dry_run: [Optional] If set to `1`, only validation is performed. Only applicable for `withdraw` using `crypto` provider and `api` type.
        :type dry_run: Optional[int]
        :param provider: [Optional] Cashier provider. `crypto` will be default option for crypto currency accounts.
        :type provider: Optional[str]
        :param type: [Optional] Data need to be returned from cashier. `api` is supported only for `crypto` provider.
        :type type: Optional[str]
        :param verification_code: [Optional] Email verification code (received from a `verify_email` call, which must be done first)
        :type verification_code: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "cashier": cashier
        }

        if address:
            data['address'] = str(address)

        if amount:
            data['amount'] = amount

        if dry_run:
            data['dry_run'] = int(dry_run)

        if provider:
            data['provider'] = str(provider)

        if type:
            data['type'] = str(type)

        if verification_code:
            data['verification_code'] = str(verification_code)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
