"""Module for Binary app_markup_details websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Optional, Union, Any, List


# https://developers.binary.com/api/#app_markup_details

class AppMarkupDetails(Base):
    """Class for Binary app_markup_details websocket channel."""

    name = "app_markup_details"

    def __call__(self, date_from: str, date_to: str, app_id: Optional[int] = None, client_loginid: Optional[str] = None, description: Optional[int] = None, limit: Optional[Union[int, float, Decimal]] = None, offset: Optional[Union[int, float, Decimal]] = None, sort: Optional[str] = None, sort_fields: Optional[List] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to app_markup_details websocket channel.
        Application: Markup Details (request)
        Retrieve details of `app_markup` according to criteria specified.
        :param date_from: Start date (epoch or YYYY-MM-DD HH:MM:SS). Results are inclusive of this time.
        :type date_from: str
        :param date_to: End date (epoch or YYYY-MM-DD HH::MM::SS). Results are inclusive of this time.
        :type date_to: str
        :param app_id: [Optional] Specific application `app_id` to report on.
        :type app_id: Optional[int]
        :param client_loginid: [Optional] Specific client loginid to report on, like CR12345
        :type client_loginid: Optional[str]
        :param description: [Optional] If set to 1, will return `app_markup` transaction details.
        :type description: Optional[int]
        :param limit: [Optional] Apply upper limit to count of transactions received.
        :type limit: Optional[Union[int, float, Decimal]]
        :param offset: [Optional] Number of transactions to skip.
        :type offset: Optional[Union[int, float, Decimal]]
        :param sort: [Optional] Sort direction on `transaction_time`. Other fields sort order is ASC.
        :type sort: Optional[str]
        :param sort_fields: [Optional] One or more of the specified fields to sort on. Default sort field is by `transaction_time`.
        :type sort_fields: Optional[List]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "app_markup_details": int(1),
            "date_from": date_from,
            "date_to": date_to
        }

        if app_id:
            data['app_id'] = int(app_id)

        if client_loginid:
            data['client_loginid'] = str(client_loginid)

        if description:
            data['description'] = int(description)

        if limit:
            data['limit'] = limit

        if offset:
            data['offset'] = offset

        if sort:
            data['sort'] = str(sort)

        if sort_fields:
            data['sort_fields'] = sort_fields

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
