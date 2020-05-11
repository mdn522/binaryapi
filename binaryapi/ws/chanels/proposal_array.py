"""Module for Binary proposal_array websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#proposal_array

class ProposalArray(Base):
    """Class for Binary proposal_array websocket chanel."""

    name = "proposal_array"

    def __call__(self, barriers, contract_type, currency: str, symbol: str, amount=None, basis: str = None, date_expiry: int = None, date_start: int = None, duration: int = None, duration_unit: str = None, multiplier=None, product_type: str = None, subscribe: bool = None, trading_period_start: int = None, passthrough=None, req_id: int = None):
        """Method to send message to proposal_array websocket chanel.
        Price Proposal: Multiple Contracts (request)
        Get latest prices for a specific contract with different barriers. **This API call is deprecated.**
        :param barriers: Array of barrier(s) for the contract.
        :type barriers: 
        :param contract_type: One or two valid contract-types.
        :type contract_type: 
        :param currency: This can only be the account-holder's currency.
        :type currency: str
        :param symbol: Symbol code.
        :type symbol: str
        :param amount: Proposed contract `payout` or `stake` value.
        :type amount: 
        :param basis: Indicate type of the `amount`.
        :type basis: str
        :param date_expiry: Epoch value of the expiry time of the contract. You must either specify `date_expiry` or duration.
        :type date_expiry: int
        :param date_start: [Optional] Indicates epoch value of the starting time of the contract. If left empty, the start time of the contract is now.
        :type date_start: int
        :param duration: Duration quantity.
        :type duration: int
        :param duration_unit: [Optional] Duration unit - `s`: seconds, `m`: minutes, `h`: hours, `d`: days, `t`: ticks.
        :type duration_unit: str
        :param multiplier: The multiplier for non-binary options. E.g. lookbacks.
        :type multiplier: 
        :param product_type: [Optional] If you specify this field, only contracts tradable through that contract type will be returned.
        :type product_type: str
        :param subscribe: [Optional] 1 - to initiate a realtime stream of prices. Note that tick trades (without a user-defined barrier), digit trades and less than 24 hours at-the-money contracts for the following underlying symbols are not streamed: `R_10`, `R_25`, `R_50`, `R_75`, `R_100`, `RDBULL`, `RDBEAR` (this is because their price is constant).
        :type subscribe: bool
        :param trading_period_start: Required only for multi-barrier trading. Defines the epoch value of the trading period start time.
        :type trading_period_start: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "proposal_array": 1,
            "barriers": barriers,
            "contract_type": contract_type,
            "currency": currency,
            "symbol": symbol
        }

        if amount:
            data['amount'] = amount

        if basis:
            data['basis'] = str(basis)

        if date_expiry:
            data['date_expiry'] = int(date_expiry)

        if date_start:
            data['date_start'] = int(date_start)

        if duration:
            data['duration'] = int(duration)

        if duration_unit:
            data['duration_unit'] = str(duration_unit)

        if multiplier:
            data['multiplier'] = multiplier

        if product_type:
            data['product_type'] = str(product_type)

        if subscribe:
            data['subscribe'] = int(subscribe)

        if trading_period_start:
            data['trading_period_start'] = int(trading_period_start)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
