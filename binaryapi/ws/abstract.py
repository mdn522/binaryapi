from binaryapi.ws.chanels.balance import Balance
from binaryapi.ws.chanels.transaction import Transaction
from binaryapi.ws.chanels.proposal import Proposal
from binaryapi.ws.chanels.buy import Buy
from binaryapi.ws.chanels.authorize import Authorize


class AbstractAPI:
    @property
    def authorize(self) -> Authorize.__call__:
        """Property for get Binary ws authorize resource.

        :returns: The instance of :class:`Authorize<binaryapi.ws.chanels.authorize.Authorize>`.
        """
        return Authorize(self).__call__

    @property
    def balance(self):
        """Property for get Binary ws balance resource.

        :returns: The instance of :class:`Balance
            <binaryapi.ws.chanels.balance.Balance>`.
        """
        return Balance(self).__call__

    @property
    def transaction(self):
        """Property for get Binary ws transaction resource.

        :returns: The instance of :class:`Transaction
            <binaryapi.ws.chanels.transaction.Transaction>`.
        """
        return Transaction(self).__call__

    @property
    def proposal(self):
        """Property for get Binary ws proposal resource.

        :returns: The instance of :class:`Proposal
            <binaryapi.ws.chanels.proposal.Proposal>`.
        """
        return Proposal(self).__call__

    @property
    def buy(self):
        """Property for get Binary ws buy resource.

        :returns: The instance of :class:`Buy
            <binaryapi.ws.chanels.buy.Buy>`.
        """
        return Buy(self).__call__
