"""Module for Binary app_register websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, List, Optional, Union
from decimal import Decimal


# https://developers.binary.com/api/#app_register

class AppRegister(Base):
    """Class for Binary app_register websocket channel."""

    name = "app_register"

    def __call__(
        self, 
        name: str, 
        scopes: List, 
        app_markup_percentage: Optional[Union[int, float, Decimal]] = None, 
        appstore: Optional[str] = None, 
        github: Optional[str] = None, 
        googleplay: Optional[str] = None, 
        homepage: Optional[str] = None, 
        redirect_uri: Optional[str] = None, 
        verification_uri: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to app_register websocket channel.
        Application: Register (request)
        Register a new OAuth application

        :param name: Application name.
        :type name: str
        :param scopes: List of permission scopes to grant the application.
        :type scopes: List
        :param app_markup_percentage: [Optional] Markup to be added to contract prices (as a percentage of contract payout).
        :type app_markup_percentage: Optional[Union[int, float, Decimal]]
        :param appstore: [Optional] Application's App Store URL (if applicable).
        :type appstore: Optional[str]
        :param github: [Optional] Application's GitHub page (for open-source projects).
        :type github: Optional[str]
        :param googleplay: [Optional] Application's Google Play URL (if applicable).
        :type googleplay: Optional[str]
        :param homepage: [Optional] Application's homepage URL.
        :type homepage: Optional[str]
        :param redirect_uri: [Optional] The URL to redirect to after a successful login. Required if charging markup percentage
        :type redirect_uri: Optional[str]
        :param verification_uri: [Optional] Used when `verify_email` called. If available, a URL containing the verification token will be sent to the client's email, otherwise only the token will be sent.
        :type verification_uri: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "app_register": int(1),
            "name": name,
            "scopes": scopes
        }

        if app_markup_percentage:
            data['app_markup_percentage'] = app_markup_percentage

        if appstore:
            data['appstore'] = str(appstore)

        if github:
            data['github'] = str(github)

        if googleplay:
            data['googleplay'] = str(googleplay)

        if homepage:
            data['homepage'] = str(homepage)

        if redirect_uri:
            data['redirect_uri'] = str(redirect_uri)

        if verification_uri:
            data['verification_uri'] = str(verification_uri)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
