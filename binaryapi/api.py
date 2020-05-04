"""Module for Binary API."""

import time
import json
import logging
import threading
from threading import Thread

import requests
import ssl
from binaryapi.ws.client import WebsocketClient
import binaryapi.global_value as global_value
from collections import defaultdict, OrderedDict


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict( n -1, type))


class BinaryAPI:
    websocket_thread: Thread
    profile = None

    def __init__(self, app_id, token):
        self.app_id = app_id
        self.token = token

        self.wss_url = "wss://ws.binaryws.com/websockets/v3?app_id={0}".format(self.app_id)

        self.websocket_client = None

    def connect(self):
        global_value.check_websocket_if_connect = None

        self.websocket_client = WebsocketClient(self)

        self.websocket_thread = threading.Thread(target=self.websocket.run_forever, kwargs={'sslopt': {
            "check_hostname": False, "cert_reqs": ssl.CERT_NONE,
            "ca_certs": "cacert.pem"}})  # for fix pyinstall error: cafile, capath and cadata cannot be all omitted
        self.websocket_thread.daemon = True
        self.websocket_thread.start()

        while True:
            try:
                if global_value.check_websocket_if_connect == 0 or global_value.check_websocket_if_connect == -1:
                    return False
                elif global_value.check_websocket_if_connect == 1:
                    break
            except:
                pass

            pass

        self.authorize()

        return True

    @property
    def websocket(self):
        """Property to get websocket.
        :returns: The instance of :class:`WebSocket <websocket.WebSocket>`.
        """
        return self.websocket_client.wss

    def authorize(self):
        self.websocket.send(json.dumps({"authorize": self.token}))

    def close(self):
        self.websocket.close()
        self.websocket_thread.join()

    def websocket_alive(self):
        return self.websocket_thread.is_alive()
