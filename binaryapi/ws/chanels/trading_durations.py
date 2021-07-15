"""Module for Binary trading_durations websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#trading_durations

class TradingDurations(Base):
    """Class for Binary trading_durations websocket channel."""

    name = "trading_durations"

    def __call__(self, landing_company: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to trading_durations websocket channel.
        Trading Durations (request)
        Retrieve a list of all available underlyings and the corresponding contract types and trading duration boundaries. If the user is logged in, only the assets available for that user's landing company will be returned.
        :param landing_company: [Optional] If specified, will return only the underlyings for the specified landing company.
        :type landing_company: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "trading_durations": int(1)
        }

        if landing_company:
            data['landing_company'] = str(landing_company)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
