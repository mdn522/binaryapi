"""Module for Binary get_financial_assessment websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#get_financial_assessment

class GetFinancialAssessment(Base):
    """Class for Binary get_financial_assessment websocket channel."""

    name = "get_financial_assessment"

    def __call__(self, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to get_financial_assessment websocket channel.
        Get Financial Assessment (request)
        This call gets the financial assessment details. The 'financial assessment' is a questionnaire that clients of certain Landing Companies need to complete, due to regulatory and KYC (know your client) requirements.
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "get_financial_assessment": int(1)
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
