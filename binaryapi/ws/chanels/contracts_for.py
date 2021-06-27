"""Module for Binary contracts_for websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#contracts_for

class ContractsFor(Base):
    """Class for Binary contracts_for websocket channel."""

    name = "contracts_for"

    def __call__(self, contracts_for: str, currency: Optional[str] = None, landing_company: Optional[str] = None, product_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to contracts_for websocket channel.
        Contracts For Symbol (request)
        For a given symbol, get the list of currently available contracts, and the latest barrier and duration limits for each contract.
        :param contracts_for: The short symbol name (obtained from `active_symbols` call).
        :type contracts_for: str
        :param currency: [Optional] Currency of the contract's stake and payout (obtained from `payout_currencies` call).
        :type currency: Optional[str]
        :param landing_company: [Optional] Indicates which landing company to get a list of contracts for. If you are logged in, your account's landing company will override this field.
        :type landing_company: Optional[str]
        :param product_type: [Optional] If you specify this field, only contracts tradable through that contract type will be returned.
        :type product_type: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "contracts_for": contracts_for
        }

        if currency:
            data['currency'] = str(currency)

        if landing_company:
            data['landing_company'] = str(landing_company)

        if product_type:
            data['product_type'] = str(product_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
