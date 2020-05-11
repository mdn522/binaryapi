"""Module for Binary statement websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#statement

class Statement(Base):
    """Class for Binary statement websocket chanel."""

    name = "statement"

    def __call__(self, action_type: str = None, date_from: int = None, date_to: int = None, description: int = None, limit=None, offset=None, passthrough=None, req_id: int = None):
        """Method to send message to statement websocket chanel.
        Statement (request)
        Retrieve a summary of account transactions, according to given search criteria
        :param action_type: [Optional] To filter the statement according to the type of transaction.
        :type action_type: str
        :param date_from: [Optional] Start date (epoch)
        :type date_from: int
        :param date_to: [Optional] End date (epoch)
        :type date_to: int
        :param description: [Optional] If set to 1, will return full contracts description.
        :type description: int
        :param limit: [Optional] Maximum number of transactions to receive.
        :type limit: 
        :param offset: [Optional] Number of transactions to skip.
        :type offset: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "statement": 1
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
