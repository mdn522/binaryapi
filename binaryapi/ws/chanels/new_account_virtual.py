"""Module for Binary new_account_virtual websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Optional, Any


# https://developers.binary.com/api/#new_account_virtual

class NewAccountVirtual(Base):
    """Class for Binary new_account_virtual websocket channel."""

    name = "new_account_virtual"

    def __call__(self, affiliate_token: Optional[str] = None, client_password: Optional[str] = None, date_first_contact: Optional[str] = None, email_consent: Optional[int] = None, gclid_url: Optional[str] = None, residence: Optional[str] = None, signup_device: Optional[str] = None, type: Optional[str] = None, utm_ad_id: Optional[str] = None, utm_adgroup_id: Optional[str] = None, utm_adrollclk_id: Optional[str] = None, utm_campaign: Optional[str] = None, utm_campaign_id: Optional[str] = None, utm_content: Optional[str] = None, utm_fbcl_id: Optional[str] = None, utm_gl_client_id: Optional[str] = None, utm_medium: Optional[str] = None, utm_msclk_id: Optional[str] = None, utm_source: Optional[str] = None, utm_term: Optional[str] = None, verification_code: Optional[str] = None, passthrough: Optional[Any] = None, req_id: Optional[int] = None):
        """Method to send message to new_account_virtual websocket channel.
        New Virtual-Money Account (request)
        Create a new virtual-money account.
        :param affiliate_token: [Optional] Affiliate token, within 32 characters.
        :type affiliate_token: Optional[str]
        :param client_password: Password (Accepts any printable ASCII character. Must be within 8-25 characters, and include numbers, lowercase and uppercase letters. Must not be the same as the user's email address).
        :type client_password: Optional[str]
        :param date_first_contact: [Optional] Date of first contact, format: `yyyy-mm-dd` in GMT timezone.
        :type date_first_contact: Optional[str]
        :param email_consent: [Optional] Boolean value: 1 or 0, indicating whether the client has given consent for marketing emails.
        :type email_consent: Optional[int]
        :param gclid_url: [Optional] Google Click Identifier to track source.
        :type gclid_url: Optional[str]
        :param residence: 2-letter country code (obtained from `residence_list` call).
        :type residence: Optional[str]
        :param signup_device: [Optional] Show whether user has used mobile or desktop.
        :type signup_device: Optional[str]
        :param type: Account type
        :type type: Optional[str]
        :param utm_ad_id: [Optional] Identifier of particular ad
        :type utm_ad_id: Optional[str]
        :param utm_adgroup_id: [Optional] Identifier of ad group in the campaign
        :type utm_adgroup_id: Optional[str]
        :param utm_adrollclk_id: [Optional] Unique identifier of click on AdRoll ads platform
        :type utm_adrollclk_id: Optional[str]
        :param utm_campaign: [Optional] Identifies a specific product promotion or strategic campaign such as a spring sale or other promotions.
        :type utm_campaign: Optional[str]
        :param utm_campaign_id: [Optional] Identifier of paid ad campaign
        :type utm_campaign_id: Optional[str]
        :param utm_content: [Optional] Used to differentiate similar content, or links within the same ad
        :type utm_content: Optional[str]
        :param utm_fbcl_id: [Optional] Unique identifier of click on Facebook ads platform
        :type utm_fbcl_id: Optional[str]
        :param utm_gl_client_id: [Optional] Unique visitor identifier on Google Ads platform.
        :type utm_gl_client_id: Optional[str]
        :param utm_medium: [Optional] Identifies the medium the link was used upon such as: email, CPC, or other methods of sharing.
        :type utm_medium: Optional[str]
        :param utm_msclk_id: [Optional] Unique click identifier on Microsoft Bing ads platform.
        :type utm_msclk_id: Optional[str]
        :param utm_source: [Optional] Identifies the source of traffic such as: search engine, newsletter, or other referral.
        :type utm_source: Optional[str]
        :param utm_term: [Optional] Used to send information related to the campaign term like paid search keywords
        :type utm_term: Optional[str]
        :param verification_code: Email verification code (received from a `verify_email` call, which must be done first).
        :type verification_code: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        """

        data = {
            "new_account_virtual": int(1)
        }

        if affiliate_token:
            data['affiliate_token'] = str(affiliate_token)

        if client_password:
            data['client_password'] = str(client_password)

        if date_first_contact:
            data['date_first_contact'] = str(date_first_contact)

        if email_consent:
            data['email_consent'] = int(email_consent)

        if gclid_url:
            data['gclid_url'] = str(gclid_url)

        if residence:
            data['residence'] = str(residence)

        if signup_device:
            data['signup_device'] = str(signup_device)

        if type:
            data['type'] = str(type)

        if utm_ad_id:
            data['utm_ad_id'] = str(utm_ad_id)

        if utm_adgroup_id:
            data['utm_adgroup_id'] = str(utm_adgroup_id)

        if utm_adrollclk_id:
            data['utm_adrollclk_id'] = str(utm_adrollclk_id)

        if utm_campaign:
            data['utm_campaign'] = str(utm_campaign)

        if utm_campaign_id:
            data['utm_campaign_id'] = str(utm_campaign_id)

        if utm_content:
            data['utm_content'] = str(utm_content)

        if utm_fbcl_id:
            data['utm_fbcl_id'] = str(utm_fbcl_id)

        if utm_gl_client_id:
            data['utm_gl_client_id'] = str(utm_gl_client_id)

        if utm_medium:
            data['utm_medium'] = str(utm_medium)

        if utm_msclk_id:
            data['utm_msclk_id'] = str(utm_msclk_id)

        if utm_source:
            data['utm_source'] = str(utm_source)

        if utm_term:
            data['utm_term'] = str(utm_term)

        if verification_code:
            data['verification_code'] = str(verification_code)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
