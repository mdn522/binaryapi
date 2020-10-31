"""Module for Binary document_upload websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#document_upload

class DocumentUpload(Base):
    """Class for Binary document_upload websocket channel."""

    name = "document_upload"

    def __call__(self, document_format: str, document_type: str, expected_checksum: str, file_size: int, document_id: Optional[str] = None, expiration_date: Optional[str] = None, page_type: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to document_upload websocket channel.
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
        :type document_id: Optional[str]
        :param expiration_date: [Optional] Document expiration date (required for Passport, Proof of ID and Driver's License)
        :type expiration_date: Optional[str]
        :param page_type: [Optional] To determine document side
        :type page_type: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "document_upload": int(1),
            "document_format": document_format,
            "document_type": document_type,
            "expected_checksum": expected_checksum,
            "file_size": int(file_size)
        }

        if document_id:
            data['document_id'] = str(document_id)

        if expiration_date:
            data['expiration_date'] = str(expiration_date)

        if page_type:
            data['page_type'] = str(page_type)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
