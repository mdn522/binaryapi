"""Module for Binary copy_start websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#copy_start

class CopyStart(Base):
    """Class for Binary copy_start websocket chanel."""

    name = "copy_start"

    def __call__(self, copy_start: str, assets=None, max_trade_stake=None, min_trade_stake=None, trade_types=None, passthrough=None, req_id: int=None):
        """Method to send message to copy_start websocket chanel.
        Copy Trading: Start (request)
        Start copy trader bets
        :param copy_start: API tokens identifying the accounts of trader which will be used to copy trades
        :type copy_start: str
        :param assets: [Optional] Used to set assets to be copied. E.x ["frxUSDJPY", "R_50"]
        :type assets: 
        :param max_trade_stake: [Optional] Used to set maximum trade stake to be copied.
        :type max_trade_stake: 
        :param min_trade_stake: [Optional] Used to set minimal trade stake to be copied.
        :type min_trade_stake: 
        :param trade_types: [Optional] Used to set trade types to be copied. E.x ["CALL", "PUT"]
        :type trade_types: 
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "copy_start": copy_start
        }

        if assets:
            data['assets'] = assets

        if max_trade_stake:
            data['max_trade_stake'] = max_trade_stake

        if min_trade_stake:
            data['min_trade_stake'] = min_trade_stake

        if trade_types:
            data['trade_types'] = trade_types

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
