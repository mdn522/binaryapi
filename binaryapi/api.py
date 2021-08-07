"""Module for Binary API."""
import decimal
import ssl
import time
import logging
from typing import Optional, Any, Union

import pause
import threading
import simplejson as json
from threading import Thread
from collections import defaultdict, OrderedDict

from binaryapi.exceptions import MessageByReqIDNotFound
from binaryapi.ws.abstract import AbstractAPI
from binaryapi.ws.client import WebsocketClient
import binaryapi.global_value as global_value

from binaryapi.ws.objects.authorize import Authorize as AuthorizeObject

DEFAULT_MAX_DICT_SIZE = 500

# noinspection PyShadowingBuiltins
def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class FixSizeOrderedDict(OrderedDict):
    # noinspection PyShadowingBuiltins
    def __init__(self, *args, max=0, **kwargs):
        self._max = max
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        if self._max > 0:
            if len(self) > self._max:
                self.popitem(False)


class BinaryAPI(AbstractAPI):
    websocket_thread: Thread
    websocket_client: WebsocketClient
    profile = AuthorizeObject()

    # message_callback: Optional[Callable] = None

    results = FixSizeOrderedDict(max=DEFAULT_MAX_DICT_SIZE)
    msg_by_req_id = FixSizeOrderedDict(max=DEFAULT_MAX_DICT_SIZE)
    msg_by_type = nested_dict(1, lambda: FixSizeOrderedDict(max=DEFAULT_MAX_DICT_SIZE))
    _request_id = 1

    def __init__(self, app_id=28035, token=None):
        self.app_id = app_id
        self.token = token

        self.message_callback = None

        self.wss_url = "wss://ws.binaryws.com/websockets/v3?app_id={0}".format(self.app_id)

        self.websocket_client = None

    def connect(self):
        global_value.check_websocket_if_connect = None

        self.websocket_client = WebsocketClient(self)

        self.websocket_thread = threading.Thread(target=self.websocket.run_forever, kwargs={
            'sslopt': {
                "check_hostname": False, "cert_reqs": ssl.CERT_NONE,
                "ca_certs": "cacert.pem"
            },
            "ping_interval": 5})  # for fix pyinstall error: cafile, capath and cadata cannot be all omitted
        self.websocket_thread.daemon = True
        self.websocket_thread.start()

        while True:
            try:
                if global_value.check_websocket_if_connect == 0 or global_value.check_websocket_if_connect == -1:
                    return False
                elif global_value.check_websocket_if_connect == 1:
                    break
            except Exception:
                pass

            pass

        if self.token:
            self.authorize(authorize=self.token)

        start_t = time.time()
        while self.profile.msg is None:
            if time.time() - start_t >= 30:
                logging.error('**error** authorize late 30 sec')
                return False

            pause.seconds(0.01)

        return True

    @property
    def websocket(self):
        """Property to get websocket.
        :returns: The instance of :class:`WebSocket <websocket.WebSocket>`.
        """
        return self.websocket_client.wss

    def close(self):
        self.websocket.close()
        self.websocket_thread.join()

    def websocket_alive(self):
        return self.websocket_thread.is_alive()

    @property
    def request_id(self):
        self._request_id += 1
        return self._request_id - 1

    def wait_for_response_by_req_id(self, req_id: int, type: Optional[str] = None, type_name: Optional[str] = None, max_timeout: Union[int, float] = 30, delay: Union[int, float] = 0.0005):
        start_time = time.time()

        type_name_repr: Optional[str] = type_name or type
        while (self.msg_by_req_id.get(req_id) is None) if type is None else (self.msg_by_type[type].get(req_id) is None):
            if time.time() - start_time >= max_timeout:
                logging.error('**warning** {}late {} sec(s)'.format(max_timeout, (type_name_repr + ' ') if type_name_repr else ''))
                # return False, None, request_id
                raise MessageByReqIDNotFound
            time.sleep(delay)
        return

    def send_websocket_request(self, name: str, msg, passthrough: Optional[Any] = None, req_id: int = None):
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
            self.msg_by_req_id[req_id] = None
            self.msg_by_type[name][req_id] = None

        if passthrough:
            msg["passthrough"] = passthrough

        def default(obj):
            if isinstance(obj, decimal.Decimal):
                return str(obj)
            raise TypeError

        data = json.dumps(msg, default=default)

        self.websocket.send(data)

        logger.debug(data)

        return req_id
