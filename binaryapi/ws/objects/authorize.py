"""Module for Binary Authorize websocket object."""
from binaryapi.ws.objects.base import Base


class Authorize(Base):
    """Class for Binary Authorize websocket object."""

    def __init__(self):
        super().__init__()
        self.__name = "authorize"
        self.__balance = None
        self.__msg = None

    # ----------------------------------------------------------------
    @property
    def balance(self):
        """Property to get balance value.

        :returns: The balance value.
        """
        return self.__balance

    @balance.setter
    def balance(self, balance):
        """Method to set balance value."""
        self.__balance = balance

    # ---------------------------------------------------------------------
    @property
    def user_id(self):
        """Property to get user id value.

        :returns: The user id value.
        """
        return self.msg.get('user_id')

    # ------------------------------------------------------------------------
    @property
    def currency(self):
        """Property to get currency value.

        :returns: The currency value.
        """
        return self.msg.get('currency')

    # ------------------------------------------------------------------------
    @property
    def is_virtual(self):
        """Property to get is_virtual value.

        :returns: The is_virtual value.
        """
        return self.msg.get('is_virtual')

    # ------------------------------------------------------------------------
    @property
    def login_id(self):
        """Property to get loginid value.

        :returns: The loginid value.
        """
        return self.msg.get('loginid')

    # ------------------------------------------------------------------------
    @property
    def scopes(self):
        """Property to get scopes value.

        :returns: The scopes value.
        """
        return self.msg.get('scopes')

    # ------------------------------------------------------------------------
    @property
    def account_list(self):
        """Property to get account_list.

        :returns: The account_list.
        """
        return self.msg.get('account_list')

    # ------------
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg
