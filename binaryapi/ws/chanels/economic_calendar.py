"""Module for Binary economic_calendar websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#economic_calendar

class EconomicCalendar(Base):
    """Class for Binary economic_calendar websocket channel."""

    name = "economic_calendar"

    def __call__(self, currency: Optional[str] = None, end_date: Optional[int] = None, start_date: Optional[int] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to economic_calendar websocket channel.
        Economic Calendar (request)
        Specify a currency to receive a list of events related to that specific currency. For example, specifying USD will return a list of USD-related events. If the currency is omitted, you will receive a list for all currencies.
        :param currency: [Optional] Currency symbol.
        :type currency: Optional[str]
        :param end_date: [Optional] End date.
        :type end_date: Optional[int]
        :param start_date: [Optional] Start date.
        :type start_date: Optional[int]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "economic_calendar": int(1)
        }

        if currency:
            data['currency'] = str(currency)

        if end_date:
            data['end_date'] = int(end_date)

        if start_date:
            data['start_date'] = int(start_date)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
