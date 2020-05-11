"""Module for Binary trading_times websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#trading_times

class TradingTimes(Base):
    """Class for Binary trading_times websocket chanel."""

    name = "trading_times"

    def __call__(self, trading_times: str, passthrough=None, req_id: int=None):
        """Method to send message to trading_times websocket chanel.
        Trading Times (request)
        Receive a list of market opening times for a given date.
        :param trading_times: Date to receive market opening times for. (`yyyy-mm-dd` format. `today` can also be specified).
        :type trading_times: str
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "trading_times": trading_times
        }



        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
