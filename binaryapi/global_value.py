from collections import defaultdict

check_websocket_if_connect = None

# TODO multi thread support
info = defaultdict(lambda: dict(
    check_websocket_if_connect=None,
))

