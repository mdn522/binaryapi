"""Module for Binary API."""
import decimal
import ssl
import time
import logging

import pause
import threading
import orjson as json
from threading import Thread
from collections import defaultdict, OrderedDict

from binaryapi.ws.client import WebsocketClient
import binaryapi.global_value as global_value

from binaryapi.ws.chanels.balance import Balance
from binaryapi.ws.chanels.transaction import Transaction
from binaryapi.ws.chanels.proposal import Proposal
from binaryapi.ws.chanels.buy import Buy
from binaryapi.ws.chanels.authorize import Authorize

from binaryapi.ws.objects.authorize import Authorize as AuthorizeObject


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class FixSizeOrderedDict(OrderedDict):
    def __init__(self, *args, max=0, **kwargs):
        self._max = max
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        if self._max > 0:
            if len(self) > self._max:
                self.popitem(False)


class BinaryAPI:
    websocket_thread: Thread
    profile = AuthorizeObject()
    message_callback = None

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
            "ca_certs": "cacert.pem"},
            "ping_interval": 5})  # for fix pyinstall error: cafile, capath and cadata cannot be all omitted
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

        self.authorize(self.token)

        start_t = time.time()
        while self.profile.msg is None:
            if time.time() - start_t >= 30:
                logging.error('**error** authorize late 30 sec')
                return False

            pause.seconds(0.0001)

        return True

    @property
    def websocket(self):
        """Property to get websocket.
        :returns: The instance of :class:`WebSocket <websocket.WebSocket>`.
        """
        return self.websocket_client.wss

    # def authorize(self):
    #     self.websocket.send(json.dumps({"authorize": self.token}))

    def close(self):
        self.websocket.close()
        self.websocket_thread.join()

    def websocket_alive(self):
        return self.websocket_thread.is_alive()

    # Code Custom
    _request_id = 100

    results = FixSizeOrderedDict(max=300)
    msg_by_request_id = FixSizeOrderedDict(max=300)
    msg_by_name = nested_dict(1, lambda: FixSizeOrderedDict(max=300))

    @property
    def request_id(self):
        self._request_id += 1
        return self._request_id - 1

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

    def send_websocket_request(self, name: str, msg, passthrough=None, req_id: int = None):
        """Send websocket request to Binary server.
        :type passthrough: dict
        :type name: str
        :param req_id: int
        :param dict msg: The websocket request msg.
        """
        logger = logging.getLogger(__name__)

        if req_id is None:
            req_id = self.request_id

        if req_id:
            msg['req_id'] = req_id
            self.results[req_id] = None
            self.msg_by_request_id[req_id] = None
            self.msg_by_name[name][req_id] = None

        if passthrough:
            msg["passthrough"] = passthrough

        def default(obj):
            if isinstance(obj, decimal.Decimal):
                return str(obj)
            raise TypeError

        data = json.dumps(msg, default=default)
        logger.debug(data)
        self.websocket.send(data)

        return req_id
