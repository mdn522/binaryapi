"""Module for Binary document_upload websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#document_upload

class DocumentUpload(Base):
    """Class for Binary document_upload websocket chanel."""

    name = "document_upload"

    def __call__(self, document_format: str, document_type: str, expected_checksum: str, file_size: int, document_id: str=None, expiration_date: str=None, page_type: str=None, passthrough=None, req_id: int=None):
        """Method to send message to document_upload websocket chanel.
        Document Upload (request)
        Request KYC information from client
        :param document_format: Document file format
        :type document_format: str
        :param document_type: Document type
        :type document_type: str
        :param expected_checksum: The checksum of the file to be uploaded
        :type expected_checksum: str
        :param file_size: Document size (should be less than 3MB)
        :type file_size: int
        :param document_id: [Optional] Document ID (required for Passport, Proof of ID and Driver's License)
        :type document_id: str
        :param expiration_date: [Optional] Document expiration date (required for Passport, Proof of ID and Driver's License)
        :type expiration_date: str
        :param page_type: [Optional] To determine document side
        :type page_type: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "document_upload": 1,
            "document_format": document_format,
            "document_type": document_type,
            "expected_checksum": expected_checksum,
            "file_size": file_size
        }

        if document_id:
            data['document_id'] = document_id

        if expiration_date:
            data['expiration_date'] = expiration_date

        if page_type:
            data['page_type'] = page_type

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
