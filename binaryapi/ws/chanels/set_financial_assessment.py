"""Module for Binary set_financial_assessment websocket channel."""
from binaryapi.ws.chanels.base import Base
from typing import Any, Optional


# https://developers.binary.com/api/#set_financial_assessment

class SetFinancialAssessment(Base):
    """Class for Binary set_financial_assessment websocket channel."""

    name = "set_financial_assessment"

    def __call__(
        self, 
        education_level: str, 
        employment_industry: str, 
        estimated_worth: str, 
        income_source: str, 
        net_income: str, 
        occupation: str, 
        account_turnover: Optional[str] = None, 
        binary_options_trading_experience: Optional[str] = None, 
        binary_options_trading_frequency: Optional[str] = None, 
        cfd_trading_experience: Optional[str] = None, 
        cfd_trading_frequency: Optional[str] = None, 
        employment_status: Optional[str] = None, 
        forex_trading_experience: Optional[str] = None, 
        forex_trading_frequency: Optional[str] = None, 
        other_instruments_trading_experience: Optional[str] = None, 
        other_instruments_trading_frequency: Optional[str] = None, 
        source_of_wealth: Optional[str] = None, 
        passthrough: Optional[Any] = None, 
        req_id: Optional[int] = None
    ) -> int:
        """Method to send message to set_financial_assessment websocket channel.
        Set Financial Assessment (request)
        This call sets the financial assessment details based on the client's answers to analyze whether they possess the experience and knowledge to understand the risks involved with binary options trading.

        :param education_level: Level of Education.
        :type education_level: str
        :param employment_industry: Industry of Employment.
        :type employment_industry: str
        :param estimated_worth: Estimated Net Worth.
        :type estimated_worth: str
        :param income_source: Income Source.
        :type income_source: str
        :param net_income: Net Annual Income.
        :type net_income: str
        :param occupation: Occupation.
        :type occupation: str
        :param account_turnover: [Optional] The anticipated account turnover.
        :type account_turnover: Optional[str]
        :param binary_options_trading_experience: [Optional] Binary options trading experience.
        :type binary_options_trading_experience: Optional[str]
        :param binary_options_trading_frequency: [Optional] Binary options trading frequency.
        :type binary_options_trading_frequency: Optional[str]
        :param cfd_trading_experience: [Optional] CFDs trading experience.
        :type cfd_trading_experience: Optional[str]
        :param cfd_trading_frequency: [Optional] CFDs trading frequency.
        :type cfd_trading_frequency: Optional[str]
        :param employment_status: [Optional] Employment Status.
        :type employment_status: Optional[str]
        :param forex_trading_experience: [Optional] Forex trading experience.
        :type forex_trading_experience: Optional[str]
        :param forex_trading_frequency: [Optional] Forex trading frequency.
        :type forex_trading_frequency: Optional[str]
        :param other_instruments_trading_experience: [Optional] Trading experience in other financial instruments.
        :type other_instruments_trading_experience: Optional[str]
        :param other_instruments_trading_frequency: [Optional] Trading frequency in other financial instruments.
        :type other_instruments_trading_frequency: Optional[str]
        :param source_of_wealth: [Optional] Source of wealth.
        :type source_of_wealth: Optional[str]
        :param passthrough: [Optional] Used to pass data through the websocket, which may be retrieved via the `echo_req` output field.
        :type passthrough: Optional[Any]
        :param req_id: [Optional] Used to map request to response.
        :type req_id: Optional[int]
        :returns: req_id
        :rtype: int
        """

        data = {
            "set_financial_assessment": int(1),
            "education_level": education_level,
            "employment_industry": employment_industry,
            "estimated_worth": estimated_worth,
            "income_source": income_source,
            "net_income": net_income,
            "occupation": occupation
        }

        if account_turnover:
            data['account_turnover'] = str(account_turnover)

        if binary_options_trading_experience:
            data['binary_options_trading_experience'] = str(binary_options_trading_experience)

        if binary_options_trading_frequency:
            data['binary_options_trading_frequency'] = str(binary_options_trading_frequency)

        if cfd_trading_experience:
            data['cfd_trading_experience'] = str(cfd_trading_experience)

        if cfd_trading_frequency:
            data['cfd_trading_frequency'] = str(cfd_trading_frequency)

        if employment_status:
            data['employment_status'] = str(employment_status)

        if forex_trading_experience:
            data['forex_trading_experience'] = str(forex_trading_experience)

        if forex_trading_frequency:
            data['forex_trading_frequency'] = str(forex_trading_frequency)

        if other_instruments_trading_experience:
            data['other_instruments_trading_experience'] = str(other_instruments_trading_experience)

        if other_instruments_trading_frequency:
            data['other_instruments_trading_frequency'] = str(other_instruments_trading_frequency)

        if source_of_wealth:
            data['source_of_wealth'] = str(source_of_wealth)

        return self.send_websocket_request(self.name, data, passthrough=passthrough, req_id=req_id)
