"""Module for Binary Buy websocket chanel."""
from binaryapi.ws.chanels.base import Base


class Buy(Base):
    """Class for Binary Buy websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "buy"

    def __call__(self, buy_id, max_price, subscribe=None, parameters=None, **kwargs):
        """Method to send message to Buy websocket chanel.
        """

        data = {
            "buy": buy_id if parameters is None else 1,
            "price": max_price,
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        if parameters:
            data['parameters'] = parameters

        # https://developers.binary.com/api/#buy

        return self.send_websocket_request(self.name, data, **kwargs)
