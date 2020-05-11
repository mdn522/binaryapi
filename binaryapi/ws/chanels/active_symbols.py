"""Module for Binary active_symbols websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#active_symbols

class ActiveSymbols(Base):
    """Class for Binary active_symbols websocket chanel."""

    name = "active_symbols"

    def __call__(self, active_symbols: str, landing_company: str = None, product_type: str = None, passthrough=None, req_id: int = None):
        """Method to send message to active_symbols websocket chanel.
        Active Symbols (request)
        Retrieve a list of all currently active symbols (underlying markets upon which contracts are available for trading).
        :param active_symbols: If you use `brief`, only a subset of fields will be returned.
        :type active_symbols: str
        :param landing_company: [Optional] If you specify this field, only symbols available for trading by that landing company will be returned. If you are logged in, only symbols available for trading by your landing company will be returned regardless of what you specify in this field.
        :type landing_company: str
        :param product_type: [Optional] If you specify this field, only symbols that can be traded through that product type will be returned.
        :type product_type: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "active_symbols": active_symbols
        }

        if landing_company:
            data['landing_company'] = str(landing_company)

        if product_type:
            data['product_type'] = str(product_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
