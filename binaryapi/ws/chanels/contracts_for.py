"""Module for Binary contracts_for websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#contracts_for

class ContractsFor(Base):
    """Class for Binary contracts_for websocket chanel."""

    name = "contracts_for"

    def __call__(self, contracts_for: str, currency: str = None, landing_company: str = None, product_type: str = None, passthrough=None, req_id: int = None):
        """Method to send message to contracts_for websocket chanel.
        Contracts For Symbol (request)
        For a given symbol, get the list of currently available contracts, and the latest barrier and duration limits for each contract.
        :param contracts_for: The short symbol name (obtained from `active_symbols` call).
        :type contracts_for: str
        :param currency: [Optional] Currency of the contract's stake and payout (obtained from `payout_currencies` call).
        :type currency: str
        :param landing_company: [Optional] Indicates which landing company to get a list of contracts for. If you are logged in, your account's landing company will override this field.
        :type landing_company: str
        :param product_type: [Optional] If you specify this field, only contracts tradable through that contract type will be returned.
        :type product_type: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
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
