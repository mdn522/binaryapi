"""Module for Binary Base websocket object."""


class Base(object):
    """Class for Binary Base websocket object."""
    # pylint: disable=too-few-public-methods

    def __init__(self):
        self.__name = None

    @property
    def name(self):
        """Property to get websocket object name.

        :returns: The name of websocket object.
        """
        return self.__name
