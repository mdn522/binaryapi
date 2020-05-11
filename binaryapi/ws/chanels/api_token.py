"""Module for Binary api_token websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#api_token

class ApiToken(Base):
    """Class for Binary api_token websocket chanel."""

    name = "api_token"

    def __call__(self, delete_token: str=None, new_token: str=None, new_token_scopes=None, valid_for_current_ip_only: int=None, passthrough=None, req_id: int=None):
        """Method to send message to api_token websocket chanel.
        API Token (request)
        This call manages API tokens
        :param delete_token: [Optional] The token to remove.
        :type delete_token: str
        :param new_token: [Optional] The name of the created token.
        :type new_token: str
        :param new_token_scopes: [Optional] List of permission scopes to provide with the token.
        :type new_token_scopes: 
        :param valid_for_current_ip_only: [Optional] If you set this parameter during token creation, then the token created will only work for the IP address that was used to create the token
        :type valid_for_current_ip_only: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "api_token": 1
        }

        if delete_token:
            data['delete_token'] = delete_token

        if new_token:
            data['new_token'] = new_token

        if new_token_scopes:
            data['new_token_scopes'] = new_token_scopes

        if valid_for_current_ip_only:
            data['valid_for_current_ip_only'] = valid_for_current_ip_only

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
