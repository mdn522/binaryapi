"""Module for Binary Proposal websocket chanel."""
from binaryapi.constants import PROPOSAL_BASIS
from binaryapi.ws.chanels.base import Base


class Proposal(Base):
    """Class for Binary Proposal websocket chanel."""
    # pylint: disable=too-few-public-methods

    name = "proposal"

    def __call__(self, contract_type, symbol, amount, basis=PROPOSAL_BASIS.STAKE, duration_unit=None, duration=None, currency=None, subscribe=None, **kwargs):
        """Method to send message to Proposal websocket chanel.
        """

        data = {
            "proposal": 1,
            "contract_type": contract_type,
            "symbol": symbol,
            "amount": amount,
            "basis": basis,
            "currency": self.api.profile.currency if currency is None else currency,
        }

        if subscribe:
            data['subscribe'] = int(subscribe)

        if duration:
            data['duration'] = int(duration)

        if duration_unit:
            data['duration_unit'] = duration_unit

        # https://developers.binary.com/api/#proposal

        return self.send_websocket_request(self.name, data, **kwargs)
