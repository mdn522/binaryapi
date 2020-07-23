"""Module for Binary proposal websocket chanel."""
from binaryapi.ws.chanels.base import Base


# https://developers.binary.com/api/#proposal

class Proposal(Base):
    """Class for Binary proposal websocket chanel."""

    name = "proposal"

    def __call__(self, contract_type: str, currency: str, symbol: str, amount=None, barrier: str = None, barrier2: str = None, basis: str = None, cancellation: str = None, date_expiry: int = None, date_start: int = None, duration: int = None, duration_unit: str = None, limit_order=None, multiplier=None, product_type: str = None, selected_tick: int = None, subscribe: bool = None, trading_period_start: int = None, passthrough=None, req_id: int = None):
        """Method to send message to proposal websocket chanel.
        Price Proposal (request)
        Gets latest price for a specific contract.
        :param contract_type: The proposed contract type
        :type contract_type: str
        :param currency: This can only be the account-holder's currency (obtained from `payout_currencies` call).
        :type currency: str
        :param symbol: The short symbol name (obtained from `active_symbols` call).
        :type symbol: str
        :param amount: [Optional] Proposed contract payout or stake, or multiplier (for lookbacks).
        :type amount: 
        :param barrier: [Optional] Barrier for the contract (or last digit prediction for digit contracts). Contracts less than 24 hours in duration would need a relative barrier (barriers which need +/-), where entry spot would be adjusted accordingly with that amount to define a barrier, except for Synthetic Indices as they support both relative and absolute barriers. Not needed for lookbacks.
        :type barrier: str
        :param barrier2: [Optional] Low barrier for the contract (for contracts with two barriers). Contracts less than 24 hours in duration would need a relative barrier (barriers which need +/-), where entry spot would be adjusted accordingly with that amount to define a barrier, except for Synthetic Indices as they support both relative and absolute barriers. Not needed for lookbacks.
        :type barrier2: str
        :param basis: [Optional] Indicates type of the `amount`.
        :type basis: str
        :param cancellation: Cancellation duration option (only for `MULTUP` and `MULTDOWN` contracts).
        :type cancellation: str
        :param date_expiry: [Optional] Epoch value of the expiry time of the contract. Either date_expiry or duration is required.
        :type date_expiry: int
        :param date_start: [Optional] Indicates epoch value of the starting time of the contract. If left empty, the start time of the contract is now.
        :type date_start: int
        :param duration: [Optional] Duration quantity. Either date_expiry or duration is required.
        :type duration: int
        :param duration_unit: [Optional] Duration unit - `s`: seconds, `m`: minutes, `h`: hours, `d`: days, `t`: ticks.
        :type duration_unit: str
        :param limit_order: Add an order to close the contract once the order condition is met (only for `MULTUP` and `MULTDOWN` contracts). Supported orders: `take_profit`, `stop_loss`.
        :type limit_order: 
        :param multiplier: [Optional] The multiplier for non-binary options. E.g. lookbacks.
        :type multiplier: 
        :param product_type: [Optional] The product type.
        :type product_type: str
        :param selected_tick: [Optional] The tick that is predicted to have the highest/lowest value - for `TICKHIGH` and `TICKLOW` contracts.
        :type selected_tick: int
        :param subscribe: [Optional] 1 - to initiate a realtime stream of prices. Note that tick trades (without a user-defined barrier), digit trades and less than 24 hours at-the-money contracts for the following underlying symbols are not streamed: `R_10`, `R_25`, `R_50`, `R_75`, `R_100`, `RDBULL`, `RDBEAR` (this is because their price is constant).
        :type subscribe: bool
        :param trading_period_start: [Optional] Required only for multi-barrier trading. Defines the epoch value of the trading period start time.
        :type trading_period_start: int
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: 
        :param req_id: [Optional] Used to map request to response.
        :type req_id: int
        """

        data = {
            "proposal": int(1),
            "contract_type": contract_type,
            "currency": currency,
            "symbol": symbol
        }

        if amount:
            data['amount'] = amount

        if barrier:
            data['barrier'] = str(barrier)

        if barrier2:
            data['barrier2'] = str(barrier2)

        if basis:
            data['basis'] = str(basis)

        if cancellation:
            data['cancellation'] = str(cancellation)

        if date_expiry:
            data['date_expiry'] = int(date_expiry)

        if date_start:
            data['date_start'] = int(date_start)

        if duration:
            data['duration'] = int(duration)

        if duration_unit:
            data['duration_unit'] = str(duration_unit)

        if limit_order:
            data['limit_order'] = limit_order

        if multiplier:
            data['multiplier'] = multiplier

        if product_type:
            data['product_type'] = str(product_type)

        if selected_tick:
            data['selected_tick'] = int(selected_tick)

        if subscribe:
            data['subscribe'] = int(subscribe)

        if trading_period_start:
            data['trading_period_start'] = int(trading_period_start)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
