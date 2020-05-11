"""Module for Binary new_account_virtual websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#new_account_virtual

class NewAccountVirtual(Base):
    """Class for Binary new_account_virtual websocket chanel."""

    name = "new_account_virtual"

    def __call__(self, client_password: str, residence: str, verification_code: str, affiliate_token: str = None, date_first_contact: str = None, gclid_url: str = None, signup_device: str = None, utm_campaign: str = None, utm_medium: str = None, utm_source: str = None, passthrough=None, req_id: int = None):
        """Method to send message to new_account_virtual websocket chanel.
        New Virtual-Money Account (request)
        Create a new virtual-money account.
        :param client_password: Password (length within 6-25 chars, accepts any printable ASCII character).
        :type client_password: str
        :param residence: 2-letter country code (obtained from `residence_list` call).
        :type residence: str
        :param verification_code: Email verification code (received from a `verify_email` call, which must be done first).
        :type verification_code: str
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: str
        :param date_first_contact: [Optional] Date of first contact, format: `yyyy-mm-dd` in GMT timezone.
        :type date_first_contact: str
        :param gclid_url: [Optional] Google Click Identifier to track source.
        :type gclid_url: str
        :param signup_device: [Optional] Show whether user has used mobile or desktop.
        :type signup_device: str
        :param utm_campaign: [Optional] Identifies a specific product promotion or strategic campaign such as a spring sale or other promotions.
        :type utm_campaign: str
        :param utm_medium: [Optional] Identifies the medium the link was used upon such as: email, CPC, or other methods of sharing.
        :type utm_medium: str
        :param utm_source: [Optional] Identifies the source of traffic such as: search engine, newsletter, or other referral.
        :type utm_source: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "new_account_virtual": 1,
            "client_password": client_password,
            "residence": residence,
            "verification_code": verification_code
        }

        if affiliate_token:
            data['affiliate_token'] = str(affiliate_token)

        if date_first_contact:
            data['date_first_contact'] = str(date_first_contact)

        if gclid_url:
            data['gclid_url'] = str(gclid_url)

        if signup_device:
            data['signup_device'] = str(signup_device)

        if utm_campaign:
            data['utm_campaign'] = str(utm_campaign)

        if utm_medium:
            data['utm_medium'] = str(utm_medium)

        if utm_source:
            data['utm_source'] = str(utm_source)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
