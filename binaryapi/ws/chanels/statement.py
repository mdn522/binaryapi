"""Module for Binary statement websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional, Union
from decimal import Decimal


# https://developers.binary.com/api/#statement

class Statement(Base):
    """Class for Binary statement websocket channel."""

    name = "statement"

    def __call__(self, action_type: Optional[str] = None, date_from: Optional[int] = None, date_to: Optional[int] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to statement websocket channel.
        Statement (request)
        Retrieve a summary of account transactions, according to given search criteria
        :param action_type: [Optional] To filter the statement according to the type of transaction.
        :type action_type: Optional[str]
        :param date_from: [Optional] Start date (epoch)
        :type date_from: Optional[int]
        :param date_to: [Optional] End date (epoch)
        :type date_to: Optional[int]
        :param description: [Optional] If set to 1, will return full contracts description.
        :type description: Optional[int]
        :param limit: [Optional] Maximum number of transactions to receive.
        :type limit: Optional[Union[int, float, Decimal]]
        :param offset: [Optional] Number of transactions to skip.
        :type offset: Optional[Union[int, float, Decimal]]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "statement": int(1)
        }

        if action_type:
            data['action_type'] = str(action_type)

        if date_from:
            data['date_from'] = int(date_from)

        if date_to:
            data['date_to'] = int(date_to)

        if description:
            data['description'] = int(description)

        if limit:
            data['limit'] = limit

        if offset:
            data['offset'] = offset

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
