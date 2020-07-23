"""Module for Binary asset_index websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#asset_index

class AssetIndex(Base):
    """Class for Binary asset_index websocket chanel."""

    name = "asset_index"

    def __call__(self, landing_company: str = None, passthrough=None, req_id: int = None):
        """Method to send message to asset_index websocket chanel.
        Asset Index (request)
        Retrieve a list of all available underlyings and the corresponding contract types and duration boundaries. If the user is logged in, only the assets available for that user's landing company will be returned.
        :param landing_company: [Optional] If specified, will return only the underlyings for the specified landing company.
        :type landing_company: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "asset_index": int(1)
        }

        if landing_company:
            data['landing_company'] = str(landing_company)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
