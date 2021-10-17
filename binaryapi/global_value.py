from collections import defaultdict

check_websocket_if_connect = None

# TODO multi thread support
info = defaultdict(lambda: dict(
    check_websocket_if_connect=None,
))

AUTO_SUBSCRIBE_TO_BALANCE: bool = True
AUTO_SUBSCRIBE_TO_TRANSACTION: bool = True

AUTO_REMOVE_SUBSCRIPTION_ID_ON_FORGET_RESPONSE = True
STORE_MSG_BY_SUBSCRIPTION = True
