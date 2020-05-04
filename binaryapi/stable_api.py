import sys

from binaryapi.api import BinaryAPI
import binaryapi.constants as OP_code
import threading
import time
import logging
import operator

from collections import defaultdict, OrderedDict
# from binaryapi.expiration import get_expiration_time, get_remaning_time
from datetime import datetime, timedelta


def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n - 1, type))


class Binary:
    def __init__(self, app_id, token):
        self.app_id = app_id
        self.token = token

        self.max_reconnect = 5
        self.connect_count = 0
        self.suspend = 0.5

        self.connect()

    def connect(self):
        while True:
            try:
                self.api.close()
            except:
                pass
                # logging.error('**warning** self.api.close() fail')
            if self.connect_count < self.max_reconnect or self.max_reconnect < 0:
                self.api = BinaryAPI(self.app_id, self.token)
                check = None

                check = self.api.connect()

                if check == True:
                    break
                time.sleep(self.suspend * 2)
                self.connect_count = self.connect_count + 1
            else:
                logging.error(
                    '**error** reconnect() too many time please look log file')
                # exit(1) # TODO

