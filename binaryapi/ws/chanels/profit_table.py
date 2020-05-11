"""Module for Binary profit_table websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#profit_table

class ProfitTable(Base):
    """Class for Binary profit_table websocket chanel."""

    name = "profit_table"

    def __call__(self, date_from: str=None, date_to: str=None, description: int=None, limit=None, offset=None, sort: str=None, passthrough=None, req_id: int=None):
        """Method to send message to profit_table websocket chanel.
        Profit Table (request)
        Retrieve a summary of account Profit Table, according to given search criteria
        :param date_from: [Optional] Start date (epoch or YYYY-MM-DD)
        :type date_from: str
        :param date_to: [Optional] End date (epoch or YYYY-MM-DD)
        :type date_to: str
        :param description: [Optional] If set to 1, will return full contracts description.
        :type description: int
        :param limit: [Optional] Apply upper limit to count of transactions received.
        :type limit: 
        :param offset: [Optional] Number of transactions to skip.
        :type offset: 
        :param sort: [Optional] Sort direction.
        :type sort: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "profit_table": 1
        }

        if date_from:
            data['date_from'] = date_from

        if date_to:
            data['date_to'] = date_to

        if description:
            data['description'] = description

        if limit:
            data['limit'] = limit

        if offset:
            data['offset'] = offset

        if sort:
            data['sort'] = sort

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
