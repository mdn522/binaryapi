"""Module for Binary websocket."""
import time

import simplejson as json
import logging

import websocket
import binaryapi.global_value as global_value
import traceback

from binaryapi.constants import MSG_TYPE


class WebsocketClient:
    def __init__(self, api):
        """
        :param api: The instance of :class:`BinaryAPI
            <binaryapi.api.BinaryAPI>`.
        """
        self.api = api
        # noinspection PyTypeChecker
        self.wss = websocket.WebSocketApp(
            self.api.wss_url, 
            on_message=self.on_message, 
            on_error=self.on_error, 
            on_close=self.on_close, 
            on_open=self.on_open
        )

    def on_message(self, ws, message):
        """Method to process websocket messages."""
        logger = logging.getLogger(__name__)
        logger.debug(message)

        message = json.loads(str(message))

        message['timestamp'] = time.time()

        msg_type = message.get('msg_type')
        req_id = message.get("req_id")

        if msg_type not in [""] and req_id:
            self.api.msg_by_req_id[req_id] = message
            self.api.msg_by_type[msg_type][req_id] = message
        # TODO callback

        # TODO error key
        if msg_type == MSG_TYPE.AUTHORIZE:  # 'authorize'
            self.api.profile.msg = message[MSG_TYPE.AUTHORIZE]

            try:
                self.api.profile.balance = message[MSG_TYPE.AUTHORIZE]["balance"]
            except Exception as e:
                pass
        elif msg_type == MSG_TYPE.BALANCE:  # 'balance'
            try:
                self.api.profile.balance = message[MSG_TYPE.BALANCE]["balance"]
            except KeyError:
                pass
        elif msg_type == MSG_TYPE.TICK:  # 'tick'
            try:
                # TODO
                pass
            except Exception as e:
                pass
        elif msg_type == MSG_TYPE.FORGET:  # 'forget'
            if global_value.AUTO_REMOVE_SUBSCRIPTION_ID_ON_FORGET_RESPONSE:
                requested_subscription_id = message['echo_req'].get('forget')
                if message[MSG_TYPE.FORGET] == 1:
                    if requested_subscription_id in self.api.subscriptions:
                        del self.api.subscriptions[requested_subscription_id]

                    if requested_subscription_id in self.api.msg_by_subscription:
                        del self.api.msg_by_subscription[requested_subscription_id]

        elif msg_type == MSG_TYPE.FORGET_ALL:  # 'forget_all'
            if global_value.AUTO_REMOVE_SUBSCRIPTION_ID_ON_FORGET_RESPONSE:
                for requested_subscription_id in message[MSG_TYPE.FORGET_ALL]:
                    if requested_subscription_id in self.api.subscriptions:
                        del self.api.subscriptions[requested_subscription_id]

                    if requested_subscription_id in self.api.msg_by_subscription:
                        del self.api.msg_by_subscription[requested_subscription_id]

        if 'subscription' in message:
            subscription_id = message['subscription']['id']
            if subscription_id not in self.api.subscriptions:
                self.api.subscriptions[subscription_id] = msg_type

            if global_value.STORE_MSG_BY_SUBSCRIPTION:
                self.api.msg_by_subscription[subscription_id].append(message)

        if self.api.message_callback is not None:  # TODO: and callable(self.api.message_callback)
            try:
                self.api.message_callback(message)
            except:
                pass

    @staticmethod
    def on_error(ws, error):  # pylint: disable=unused-argument
        """Method to process websocket errors."""
        logger = logging.getLogger(__name__)
        logger.error(error)
        global_value.check_websocket_if_connect = -1

    @staticmethod
    def on_open(ws):  # pylint: disable=unused-argument
        """Method to process websocket open."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket client connected.")
        global_value.check_websocket_if_connect = 1

    @staticmethod
    def on_close(ws, *args, **kwargs):  # pylint: disable=unused-argument
        """Method to process websocket close."""
        logger = logging.getLogger(__name__)
        logger.debug("Websocket connection closed.")
        global_value.check_websocket_if_connect = 0
