"""Module for Binary ticks_history websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union


# https://developers.binary.com/api/#ticks_history

class TicksHistory(Base):
    """Class for Binary ticks_history websocket channel."""

    name = "ticks_history"

    def __call__(
        self, 
        ticks_history: str, 
        end: str, 
        adjust_start_time: Optional[int] = None, 
        count: Optional[int] = None, 
        granularity: Optional[int] = None, 
        start: Optional[int] = None, 
        style: Optional[str] = None, 
        subscribe: Optional[Union[bool, int]] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to ticks_history websocket channel.
        Ticks History (request)
        Get historic tick data for a given symbol.

        :param ticks_history: Short symbol name (obtained from the `active_symbols` call).
        :type ticks_history: str
        :param end: Epoch value representing the latest boundary of the returned ticks. If `latest` is specified, this will be the latest available timestamp.
        :type end: str
        :param adjust_start_time: [Optional] 1 - if the market is closed at the end time, or license limit is before end time, adjust interval backwards to compensate.
        :type adjust_start_time: Optional[int]
        :param count: [Optional] An upper limit on ticks to receive.
        :type count: Optional[int]
        :param granularity: [Optional] Only applicable for style: `candles`. Candle time-dimension width setting. (default: `60`).
        :type granularity: Optional[int]
        :param start: [Optional] Epoch value representing the earliest boundary of the returned ticks. 
- For `"style": "ticks"`: this will default to 1 day ago.
- For `"style": "candles"`: it will default to 1 day ago if count or granularity is undefined.
        :type start: Optional[int]
        :param style: [Optional] The tick-output style.
        :type style: Optional[str]
        :param subscribe: [Optional] 1 - to send updates whenever a new tick is received.
        :type subscribe: Optional[Union[bool, int]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "ticks_history": ticks_history,
            "end": end
        }

        if adjust_start_time:
            data['adjust_start_time'] = int(adjust_start_time)

        if count:
            data['count'] = int(count)

        if granularity:
            data['granularity'] = int(granularity)

        if start:
            data['start'] = int(start)

        if style:
            data['style'] = str(style)

        if subscribe:
            data['subscribe'] = int(subscribe)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
