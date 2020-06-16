"""Module for Binary websocket."""

import orjson as json
import logging

import websocket
import binaryapi.global_value as global_value


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

    def on_message(self, message):
        """Method to process websocket messages."""
        logger = logging.getLogger(__name__)
        logger.debug(message)

        message = json.loads(str(message))
        msg_type = message.get('msg_type')

        if msg_type not in [""] and message.get("req_id"):
            self.api.msg_by_req_id[message.get("req_id")] = message
            self.api.msg_by_type[msg_type][message.get("req_id")] = message
        # TODO callback

        # TODO error key
        if msg_type == 'authorize':
            self.api.profile.msg = message["authorize"]

            try:
                self.api.profile.balance = message["authorize"]["balance"]
            except Exception as e:
                pass
        elif msg_type == 'balance':
            self.api.profile.balance = message["balance"]["balance"]
            pass

        if self.api.message_callback is not None:
            self.api.message_callback(message)

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
