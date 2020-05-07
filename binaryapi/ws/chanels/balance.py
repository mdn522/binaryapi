"""Module for Binary Balance websocket chanel."""
import datetime

from binaryapi.ws.chanels.base import Base


class Balance(Base):
    """Class for Binary Balance websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "balance"

    def __call__(self, subscribe=True, account=None, **kwargs):
        """Method to send message to Balance websocket chanel.
        :type account: str
        :type subscribe: bool
        
        """

        data = {
            "balance": 1,
            "subscribe": int(subscribe),
        }

        if account:
            data['account'] = account

        # TODO passthrough
        # https://developers.binary.com/api/#balance

        return self.send_websocket_request(self.name, data, **kwargs)
