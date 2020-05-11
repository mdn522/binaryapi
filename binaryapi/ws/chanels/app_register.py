"""Module for Binary app_register websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#app_register

class AppRegister(Base):
    """Class for Binary app_register websocket chanel."""

    name = "app_register"

    def __call__(self, name: str, redirect_uri: str, scopes, app_markup_percentage=None, appstore: str=None, github: str=None, googleplay: str=None, homepage: str=None, verification_uri: str=None, passthrough=None, req_id: int=None):
        """Method to send message to app_register websocket chanel.
        Application: Register (request)
        Register a new OAuth application
        :param name: Application name.
        :type name: str
        :param redirect_uri: The URL to redirect to after a successful login.
        :type redirect_uri: str
        :param scopes: List of permission scopes to grant the application.
        :type scopes: 
        :param app_markup_percentage: [Optional] Markup to be added to contract prices (as a percentage of contract payout).
        :type app_markup_percentage: 
        :param appstore: [Optional] Application's App Store URL (if applicable).
        :type appstore: str
        :param github: [Optional] Application's GitHub page (for open-source projects).
        :type github: str
        :param googleplay: [Optional] Application's Google Play URL (if applicable).
        :type googleplay: str
        :param homepage: [Optional] Application's homepage URL.
        :type homepage: str
        :param verification_uri: [Optional] Used when `verify_email` called. If available, a URL containing the verification token will be sent to the client's email, otherwise only the token will be sent.
        :type verification_uri: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "app_register": 1,
            "name": name,
            "redirect_uri": redirect_uri,
            "scopes": scopes
        }

        if app_markup_percentage:
            data['app_markup_percentage'] = app_markup_percentage

        if appstore:
            data['appstore'] = appstore

        if github:
            data['github'] = github

        if googleplay:
            data['googleplay'] = googleplay

        if homepage:
            data['homepage'] = homepage

        if verification_uri:
            data['verification_uri'] = verification_uri

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
