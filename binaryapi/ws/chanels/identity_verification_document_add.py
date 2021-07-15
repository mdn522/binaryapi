"""Module for Binary identity_verification_document_add websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#identity_verification_document_add

class IdentityVerificationDocumentAdd(Base):
    """Class for Binary identity_verification_document_add websocket channel."""

    name = "identity_verification_document_add"

    def __call__(self, document_number: str, document_type: str, issuing_country: str, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to identity_verification_document_add websocket channel.
        Identity Verification Add Document (request)
        Add document information such as issuing country, type and id for IDV processing.
        :param document_number: The unique identification number on the provided document.
        :type document_number: str
        :param document_type: Type of the document provided by the user, e.g. national_id, passport, etc (obtained from `residence_list` call).
        :type document_type: str
        :param issuing_country: 2-letter country code (obtained from `residence_list` call).
        :type issuing_country: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "identity_verification_document_add": int(1),
            "document_number": document_number,
            "document_type": document_type,
            "issuing_country": issuing_country
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
