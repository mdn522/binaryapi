"""Module for Binary landing_company_details websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#landing_company_details

class LandingCompanyDetails(Base):
    """Class for Binary landing_company_details websocket chanel."""

    name = "landing_company_details"

    def __call__(self, landing_company_details: str, passthrough=None, req_id: int=None):
        """Method to send message to landing_company_details websocket chanel.
        Landing Company Details (request)
        The company has a number of licensed subsidiaries in various jurisdictions, which are called Landing Companies (and which are wholly owned subsidiaries of the Binary Group). This call provides information about each Landing Company.
        :param landing_company_details: Landing company shortcode.
        :type landing_company_details: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "landing_company_details": landing_company_details
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
