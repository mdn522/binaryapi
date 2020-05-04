"""Module for Binary websocket."""

import json
import logging
from collections import OrderedDict

import websocket
import binaryapi.constants as OP_code
import binaryapi.global_value as global_value

import time


class WebsocketClient:
    def __init__(self, api):
        """
        :param api: The instance of :class:`BinaryAPI
            <binaryapi.api.BinaryAPI>`.
        """
        self.api = api
        self.wss = websocket.WebSocketApp(
            self.api.wss_url, on_message=self.on_message,
            on_error=self.on_error, on_close=self.on_close,
            on_open=self.on_open)

    @staticmethod
    def on_message(self, message):
        """Method to process websocket messages."""
        logger = logging.getLogger(__name__)
        logger.debug(message)

        message = json.loads(str(message))

        if (message['msg_type'] == 'authorize'):
            # TODO
            pass

        print('-> %s' % message)

    @staticmethod
    def on_error(wss, error):  # pylint: disable=unused-argument
        """Method to process websocket errors."""
        logger = logging.getLogger(__name__)
        logger.error(error)
        global_value.check_websocket_if_connect = -1

    @staticmethod
    def on_open(wss):  # pylint: disable=unused-argument
        """Method to process websocket open."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket client connected.")
        global_value.check_websocket_if_connect = 1

    @staticmethod
    def on_close(wss):  # pylint: disable=unused-argument
        """Method to process websocket close."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket connection closed.")
        global_value.check_websocket_if_connect = 0
