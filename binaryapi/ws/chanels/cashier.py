"""Module for Binary cashier websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#cashier

class Cashier(Base):
    """Class for Binary cashier websocket channel."""

    name = "cashier"

    def __call__(self, cashier: str, provider: Optional[str] = None, type: Optional[str] = None, verification_code: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to cashier websocket channel.
        Cashier Information (request)
        Request the cashier info for the specified type.
        :param cashier: Operation which needs to be requested from cashier
        :type cashier: str
        :param provider: [Optional] Cashier provider. `crypto` will be default option for crypto currency accounts.
        :type provider: Optional[str]
        :param type: [Optional] Data need to be returned from cashier. `api` is supported only for `crypto` provider with `deposit` operation.
        :type type: Optional[str]
        :param verification_code: [Optional] Email verification code (received from a `verify_email` call, which must be done first)
        :type verification_code: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "cashier": cashier
        }

        if provider:
            data['provider'] = str(provider)

        if type:
            data['type'] = str(type)

        if verification_code:
            data['verification_code'] = str(verification_code)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
