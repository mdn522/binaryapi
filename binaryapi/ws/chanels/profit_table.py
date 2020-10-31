"""Module for Binary profit_table websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Any, Union, Optional


# https://developers.binary.com/api/#profit_table

class ProfitTable(Base):
    """Class for Binary profit_table websocket channel."""

    name = "profit_table"

    def __call__(self, date_from: Optional[str] = None, date_to: Optional[str] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, sort: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to profit_table websocket channel.
        Profit Table (request)
        Retrieve a summary of account Profit Table, according to given search criteria
        :param date_from: [Optional] Start date (epoch or YYYY-MM-DD)
        :type date_from: Optional[str]
        :param date_to: [Optional] End date (epoch or YYYY-MM-DD)
        :type date_to: Optional[str]
        :param description: [Optional] If set to 1, will return full contracts description.
        :type description: Optional[int]
        :param limit: [Optional] Apply upper limit to count of transactions received.
        :type limit: Optional[Union[int, float, Decimal]]
        :param offset: [Optional] Number of transactions to skip.
        :type offset: Optional[Union[int, float, Decimal]]
        :param sort: [Optional] Sort direction.
        :type sort: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "profit_table": int(1)
        }

        if date_from:
            data['date_from'] = str(date_from)

        if date_to:
            data['date_to'] = str(date_to)

        if description:
            data['description'] = int(description)

        if limit:
            data['limit'] = limit

        if offset:
            data['offset'] = offset

        if sort:
            data['sort'] = str(sort)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
