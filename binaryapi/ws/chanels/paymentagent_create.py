"""Module for Binary paymentagent_create websocket channel."""
from binaryapi.ws.chanels.base import Base
from decimal import Decimal
from typing import Optional, Union, Any, List


# https://developers.binary.com/api/#paymentagent_create

class PaymentagentCreate(Base):
    """Class for Binary paymentagent_create websocket channel."""

    name = "paymentagent_create"

    def __call__(self, code_of_conduct_approval: int, commission_deposit: Union[int, float, Decimal], commission_withdrawal: Union[int, float, Decimal], email: str, information: str, payment_agent_name: str, supported_payment_methods: List, url: str, affiliate_id: Optional[str] = None, phone: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to paymentagent_create websocket channel.
        Payment agent create (request)
        Saves client's payment agent details.
        :param code_of_conduct_approval: Indicates client's agreement with the Code of Conduct.
        :type code_of_conduct_approval: int
        :param commission_deposit: Commission  (%) the agent wants to take on deposits
        :type commission_deposit: Union[int, float, Decimal]
        :param commission_withdrawal: Commission  (%) the agent wants to take on withdrawals
        :type commission_withdrawal: Union[int, float, Decimal]
        :param email: Payment agent's email address.
        :type email: str
        :param information: [Optional] Information about payment agent and their proposed service.
        :type information: str
        :param payment_agent_name: The name with which the payment agent is going to be identified.
        :type payment_agent_name: str
        :param supported_payment_methods: A list of supported payment methods.
        :type supported_payment_methods: List
        :param url: The URL of payment agent's website.
        :type url: str
        :param affiliate_id: [Optional] Client's My Affiliate id, if exists.
        :type affiliate_id: Optional[str]
        :param phone: Payment agent's phone number with coutry code.
        :type phone: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "paymentagent_create": int(1),
            "code_of_conduct_approval": int(code_of_conduct_approval),
            "commission_deposit": commission_deposit,
            "commission_withdrawal": commission_withdrawal,
            "email": email,
            "information": information,
            "payment_agent_name": payment_agent_name,
            "supported_payment_methods": supported_payment_methods,
            "url": url
        }

        if affiliate_id:
            data['affiliate_id'] = str(affiliate_id)

        if phone:
            data['phone'] = str(phone)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
