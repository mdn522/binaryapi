## This code is auto-generated.
from binaryapi.ws.chanels.active_symbols import ActiveSymbols
from binaryapi.ws.chanels.api_token import ApiToken
from binaryapi.ws.chanels.app_delete import AppDelete
from binaryapi.ws.chanels.app_get import AppGet
from binaryapi.ws.chanels.app_list import AppList
from binaryapi.ws.chanels.app_markup_details import AppMarkupDetails
from binaryapi.ws.chanels.app_register import AppRegister
from binaryapi.ws.chanels.app_update import AppUpdate
from binaryapi.ws.chanels.asset_index import AssetIndex
from binaryapi.ws.chanels.authorize import Authorize
from binaryapi.ws.chanels.balance import Balance
from binaryapi.ws.chanels.buy import Buy
from binaryapi.ws.chanels.buy_contract_for_multiple_accounts import BuyContractForMultipleAccounts
from binaryapi.ws.chanels.cancel import Cancel
from binaryapi.ws.chanels.cashier import Cashier
from binaryapi.ws.chanels.contracts_for import ContractsFor
from binaryapi.ws.chanels.contract_update import ContractUpdate
from binaryapi.ws.chanels.contract_update_history import ContractUpdateHistory
from binaryapi.ws.chanels.copytrading_list import CopytradingList
from binaryapi.ws.chanels.copytrading_statistics import CopytradingStatistics
from binaryapi.ws.chanels.copy_start import CopyStart
from binaryapi.ws.chanels.copy_stop import CopyStop
from binaryapi.ws.chanels.document_upload import DocumentUpload
from binaryapi.ws.chanels.exchange_rates import ExchangeRates
from binaryapi.ws.chanels.forget import Forget
from binaryapi.ws.chanels.forget_all import ForgetAll
from binaryapi.ws.chanels.get_account_status import GetAccountStatus
from binaryapi.ws.chanels.get_financial_assessment import GetFinancialAssessment
from binaryapi.ws.chanels.get_limits import GetLimits
from binaryapi.ws.chanels.get_self_exclusion import GetSelfExclusion
from binaryapi.ws.chanels.get_settings import GetSettings
from binaryapi.ws.chanels.landing_company import LandingCompany
from binaryapi.ws.chanels.landing_company_details import LandingCompanyDetails
from binaryapi.ws.chanels.login_history import LoginHistory
from binaryapi.ws.chanels.logout import Logout
from binaryapi.ws.chanels.mt5_deposit import Mt5Deposit
from binaryapi.ws.chanels.mt5_get_settings import Mt5GetSettings
from binaryapi.ws.chanels.mt5_login_list import Mt5LoginList
from binaryapi.ws.chanels.mt5_new_account import Mt5NewAccount
from binaryapi.ws.chanels.mt5_password_change import Mt5PasswordChange
from binaryapi.ws.chanels.mt5_password_check import Mt5PasswordCheck
from binaryapi.ws.chanels.mt5_password_reset import Mt5PasswordReset
from binaryapi.ws.chanels.mt5_withdrawal import Mt5Withdrawal
from binaryapi.ws.chanels.new_account_maltainvest import NewAccountMaltainvest
from binaryapi.ws.chanels.new_account_real import NewAccountReal
from binaryapi.ws.chanels.new_account_virtual import NewAccountVirtual
from binaryapi.ws.chanels.oauth_apps import OauthApps
from binaryapi.ws.chanels.p2p_advertiser_adverts import P2PAdvertiserAdverts
from binaryapi.ws.chanels.p2p_advertiser_create import P2PAdvertiserCreate
from binaryapi.ws.chanels.p2p_advertiser_info import P2PAdvertiserInfo
from binaryapi.ws.chanels.p2p_advertiser_update import P2PAdvertiserUpdate
from binaryapi.ws.chanels.p2p_advert_create import P2PAdvertCreate
from binaryapi.ws.chanels.p2p_advert_info import P2PAdvertInfo
from binaryapi.ws.chanels.p2p_advert_list import P2PAdvertList
from binaryapi.ws.chanels.p2p_advert_update import P2PAdvertUpdate
from binaryapi.ws.chanels.p2p_chat_create import P2PChatCreate
from binaryapi.ws.chanels.p2p_order_cancel import P2POrderCancel
from binaryapi.ws.chanels.p2p_order_confirm import P2POrderConfirm
from binaryapi.ws.chanels.p2p_order_create import P2POrderCreate
from binaryapi.ws.chanels.p2p_order_info import P2POrderInfo
from binaryapi.ws.chanels.p2p_order_list import P2POrderList
from binaryapi.ws.chanels.paymentagent_list import PaymentagentList
from binaryapi.ws.chanels.paymentagent_transfer import PaymentagentTransfer
from binaryapi.ws.chanels.paymentagent_withdraw import PaymentagentWithdraw
from binaryapi.ws.chanels.payout_currencies import PayoutCurrencies
from binaryapi.ws.chanels.ping import Ping
from binaryapi.ws.chanels.portfolio import Portfolio
from binaryapi.ws.chanels.profit_table import ProfitTable
from binaryapi.ws.chanels.proposal import Proposal
from binaryapi.ws.chanels.proposal_array import ProposalArray
from binaryapi.ws.chanels.proposal_open_contract import ProposalOpenContract
from binaryapi.ws.chanels.reality_check import RealityCheck
from binaryapi.ws.chanels.residence_list import ResidenceList
from binaryapi.ws.chanels.revoke_oauth_app import RevokeOauthApp
from binaryapi.ws.chanels.sell import Sell
from binaryapi.ws.chanels.sell_contract_for_multiple_accounts import SellContractForMultipleAccounts
from binaryapi.ws.chanels.sell_expired import SellExpired
from binaryapi.ws.chanels.set_account_currency import SetAccountCurrency
from binaryapi.ws.chanels.set_financial_assessment import SetFinancialAssessment
from binaryapi.ws.chanels.set_self_exclusion import SetSelfExclusion
from binaryapi.ws.chanels.set_settings import SetSettings
from binaryapi.ws.chanels.statement import Statement
from binaryapi.ws.chanels.states_list import StatesList
from binaryapi.ws.chanels.ticks import Ticks
from binaryapi.ws.chanels.ticks_history import TicksHistory
from binaryapi.ws.chanels.time import Time
from binaryapi.ws.chanels.tnc_approval import TncApproval
from binaryapi.ws.chanels.topup_virtual import TopupVirtual
from binaryapi.ws.chanels.trading_durations import TradingDurations
from binaryapi.ws.chanels.trading_times import TradingTimes
from binaryapi.ws.chanels.transaction import Transaction
from binaryapi.ws.chanels.transfer_between_accounts import TransferBetweenAccounts
from binaryapi.ws.chanels.verify_email import VerifyEmail
from binaryapi.ws.chanels.website_status import WebsiteStatus


class AbstractAPI:
    @property
    def active_symbols(self):
        """Property for get Binary ws active_symbols resource.

        :returns: The instance of :class:`ActiveSymbols<binaryapi.ws.chanels.active_symbols.ActiveSymbols>`.
        """
        return ActiveSymbols(self).__call__

    @property
    def api_token(self):
        """Property for get Binary ws api_token resource.

        :returns: The instance of :class:`ApiToken<binaryapi.ws.chanels.api_token.ApiToken>`.
        """
        return ApiToken(self).__call__

    @property
    def app_delete(self):
        """Property for get Binary ws app_delete resource.

        :returns: The instance of :class:`AppDelete<binaryapi.ws.chanels.app_delete.AppDelete>`.
        """
        return AppDelete(self).__call__

    @property
    def app_get(self):
        """Property for get Binary ws app_get resource.

        :returns: The instance of :class:`AppGet<binaryapi.ws.chanels.app_get.AppGet>`.
        """
        return AppGet(self).__call__

    @property
    def app_list(self):
        """Property for get Binary ws app_list resource.

        :returns: The instance of :class:`AppList<binaryapi.ws.chanels.app_list.AppList>`.
        """
        return AppList(self).__call__

    @property
    def app_markup_details(self):
        """Property for get Binary ws app_markup_details resource.

        :returns: The instance of :class:`AppMarkupDetails<binaryapi.ws.chanels.app_markup_details.AppMarkupDetails>`.
        """
        return AppMarkupDetails(self).__call__

    @property
    def app_register(self):
        """Property for get Binary ws app_register resource.

        :returns: The instance of :class:`AppRegister<binaryapi.ws.chanels.app_register.AppRegister>`.
        """
        return AppRegister(self).__call__

    @property
    def app_update(self):
        """Property for get Binary ws app_update resource.

        :returns: The instance of :class:`AppUpdate<binaryapi.ws.chanels.app_update.AppUpdate>`.
        """
        return AppUpdate(self).__call__

    @property
    def asset_index(self):
        """Property for get Binary ws asset_index resource.

        :returns: The instance of :class:`AssetIndex<binaryapi.ws.chanels.asset_index.AssetIndex>`.
        """
        return AssetIndex(self).__call__

    @property
    def authorize(self):
        """Property for get Binary ws authorize resource.

        :returns: The instance of :class:`Authorize<binaryapi.ws.chanels.authorize.Authorize>`.
        """
        return Authorize(self).__call__

    @property
    def balance(self):
        """Property for get Binary ws balance resource.

        :returns: The instance of :class:`Balance<binaryapi.ws.chanels.balance.Balance>`.
        """
        return Balance(self).__call__

    @property
    def buy(self):
        """Property for get Binary ws buy resource.

        :returns: The instance of :class:`Buy<binaryapi.ws.chanels.buy.Buy>`.
        """
        return Buy(self).__call__

    @property
    def buy_contract_for_multiple_accounts(self):
        """Property for get Binary ws buy_contract_for_multiple_accounts resource.

        :returns: The instance of :class:`BuyContractForMultipleAccounts<binaryapi.ws.chanels.buy_contract_for_multiple_accounts.BuyContractForMultipleAccounts>`.
        """
        return BuyContractForMultipleAccounts(self).__call__

    @property
    def cancel(self):
        """Property for get Binary ws cancel resource.

        :returns: The instance of :class:`Cancel<binaryapi.ws.chanels.cancel.Cancel>`.
        """
        return Cancel(self).__call__

    @property
    def cashier(self):
        """Property for get Binary ws cashier resource.

        :returns: The instance of :class:`Cashier<binaryapi.ws.chanels.cashier.Cashier>`.
        """
        return Cashier(self).__call__

    @property
    def contracts_for(self):
        """Property for get Binary ws contracts_for resource.

        :returns: The instance of :class:`ContractsFor<binaryapi.ws.chanels.contracts_for.ContractsFor>`.
        """
        return ContractsFor(self).__call__

    @property
    def contract_update(self):
        """Property for get Binary ws contract_update resource.

        :returns: The instance of :class:`ContractUpdate<binaryapi.ws.chanels.contract_update.ContractUpdate>`.
        """
        return ContractUpdate(self).__call__

    @property
    def contract_update_history(self):
        """Property for get Binary ws contract_update_history resource.

        :returns: The instance of :class:`ContractUpdateHistory<binaryapi.ws.chanels.contract_update_history.ContractUpdateHistory>`.
        """
        return ContractUpdateHistory(self).__call__

    @property
    def copytrading_list(self):
        """Property for get Binary ws copytrading_list resource.

        :returns: The instance of :class:`CopytradingList<binaryapi.ws.chanels.copytrading_list.CopytradingList>`.
        """
        return CopytradingList(self).__call__

    @property
    def copytrading_statistics(self):
        """Property for get Binary ws copytrading_statistics resource.

        :returns: The instance of :class:`CopytradingStatistics<binaryapi.ws.chanels.copytrading_statistics.CopytradingStatistics>`.
        """
        return CopytradingStatistics(self).__call__

    @property
    def copy_start(self):
        """Property for get Binary ws copy_start resource.

        :returns: The instance of :class:`CopyStart<binaryapi.ws.chanels.copy_start.CopyStart>`.
        """
        return CopyStart(self).__call__

    @property
    def copy_stop(self):
        """Property for get Binary ws copy_stop resource.

        :returns: The instance of :class:`CopyStop<binaryapi.ws.chanels.copy_stop.CopyStop>`.
        """
        return CopyStop(self).__call__

    @property
    def document_upload(self):
        """Property for get Binary ws document_upload resource.

        :returns: The instance of :class:`DocumentUpload<binaryapi.ws.chanels.document_upload.DocumentUpload>`.
        """
        return DocumentUpload(self).__call__

    @property
    def exchange_rates(self):
        """Property for get Binary ws exchange_rates resource.

        :returns: The instance of :class:`ExchangeRates<binaryapi.ws.chanels.exchange_rates.ExchangeRates>`.
        """
        return ExchangeRates(self).__call__

    @property
    def forget(self):
        """Property for get Binary ws forget resource.

        :returns: The instance of :class:`Forget<binaryapi.ws.chanels.forget.Forget>`.
        """
        return Forget(self).__call__

    @property
    def forget_all(self):
        """Property for get Binary ws forget_all resource.

        :returns: The instance of :class:`ForgetAll<binaryapi.ws.chanels.forget_all.ForgetAll>`.
        """
        return ForgetAll(self).__call__

    @property
    def get_account_status(self):
        """Property for get Binary ws get_account_status resource.

        :returns: The instance of :class:`GetAccountStatus<binaryapi.ws.chanels.get_account_status.GetAccountStatus>`.
        """
        return GetAccountStatus(self).__call__

    @property
    def get_financial_assessment(self):
        """Property for get Binary ws get_financial_assessment resource.

        :returns: The instance of :class:`GetFinancialAssessment<binaryapi.ws.chanels.get_financial_assessment.GetFinancialAssessment>`.
        """
        return GetFinancialAssessment(self).__call__

    @property
    def get_limits(self):
        """Property for get Binary ws get_limits resource.

        :returns: The instance of :class:`GetLimits<binaryapi.ws.chanels.get_limits.GetLimits>`.
        """
        return GetLimits(self).__call__

    @property
    def get_self_exclusion(self):
        """Property for get Binary ws get_self_exclusion resource.

        :returns: The instance of :class:`GetSelfExclusion<binaryapi.ws.chanels.get_self_exclusion.GetSelfExclusion>`.
        """
        return GetSelfExclusion(self).__call__

    @property
    def get_settings(self):
        """Property for get Binary ws get_settings resource.

        :returns: The instance of :class:`GetSettings<binaryapi.ws.chanels.get_settings.GetSettings>`.
        """
        return GetSettings(self).__call__

    @property
    def landing_company(self):
        """Property for get Binary ws landing_company resource.

        :returns: The instance of :class:`LandingCompany<binaryapi.ws.chanels.landing_company.LandingCompany>`.
        """
        return LandingCompany(self).__call__

    @property
    def landing_company_details(self):
        """Property for get Binary ws landing_company_details resource.

        :returns: The instance of :class:`LandingCompanyDetails<binaryapi.ws.chanels.landing_company_details.LandingCompanyDetails>`.
        """
        return LandingCompanyDetails(self).__call__

    @property
    def login_history(self):
        """Property for get Binary ws login_history resource.

        :returns: The instance of :class:`LoginHistory<binaryapi.ws.chanels.login_history.LoginHistory>`.
        """
        return LoginHistory(self).__call__

    @property
    def logout(self):
        """Property for get Binary ws logout resource.

        :returns: The instance of :class:`Logout<binaryapi.ws.chanels.logout.Logout>`.
        """
        return Logout(self).__call__

    @property
    def mt5_deposit(self):
        """Property for get Binary ws mt5_deposit resource.

        :returns: The instance of :class:`Mt5Deposit<binaryapi.ws.chanels.mt5_deposit.Mt5Deposit>`.
        """
        return Mt5Deposit(self).__call__

    @property
    def mt5_get_settings(self):
        """Property for get Binary ws mt5_get_settings resource.

        :returns: The instance of :class:`Mt5GetSettings<binaryapi.ws.chanels.mt5_get_settings.Mt5GetSettings>`.
        """
        return Mt5GetSettings(self).__call__

    @property
    def mt5_login_list(self):
        """Property for get Binary ws mt5_login_list resource.

        :returns: The instance of :class:`Mt5LoginList<binaryapi.ws.chanels.mt5_login_list.Mt5LoginList>`.
        """
        return Mt5LoginList(self).__call__

    @property
    def mt5_new_account(self):
        """Property for get Binary ws mt5_new_account resource.

        :returns: The instance of :class:`Mt5NewAccount<binaryapi.ws.chanels.mt5_new_account.Mt5NewAccount>`.
        """
        return Mt5NewAccount(self).__call__

    @property
    def mt5_password_change(self):
        """Property for get Binary ws mt5_password_change resource.

        :returns: The instance of :class:`Mt5PasswordChange<binaryapi.ws.chanels.mt5_password_change.Mt5PasswordChange>`.
        """
        return Mt5PasswordChange(self).__call__

    @property
    def mt5_password_check(self):
        """Property for get Binary ws mt5_password_check resource.

        :returns: The instance of :class:`Mt5PasswordCheck<binaryapi.ws.chanels.mt5_password_check.Mt5PasswordCheck>`.
        """
        return Mt5PasswordCheck(self).__call__

    @property
    def mt5_password_reset(self):
        """Property for get Binary ws mt5_password_reset resource.

        :returns: The instance of :class:`Mt5PasswordReset<binaryapi.ws.chanels.mt5_password_reset.Mt5PasswordReset>`.
        """
        return Mt5PasswordReset(self).__call__

    @property
    def mt5_withdrawal(self):
        """Property for get Binary ws mt5_withdrawal resource.

        :returns: The instance of :class:`Mt5Withdrawal<binaryapi.ws.chanels.mt5_withdrawal.Mt5Withdrawal>`.
        """
        return Mt5Withdrawal(self).__call__

    @property
    def new_account_maltainvest(self):
        """Property for get Binary ws new_account_maltainvest resource.

        :returns: The instance of :class:`NewAccountMaltainvest<binaryapi.ws.chanels.new_account_maltainvest.NewAccountMaltainvest>`.
        """
        return NewAccountMaltainvest(self).__call__

    @property
    def new_account_real(self):
        """Property for get Binary ws new_account_real resource.

        :returns: The instance of :class:`NewAccountReal<binaryapi.ws.chanels.new_account_real.NewAccountReal>`.
        """
        return NewAccountReal(self).__call__

    @property
    def new_account_virtual(self):
        """Property for get Binary ws new_account_virtual resource.

        :returns: The instance of :class:`NewAccountVirtual<binaryapi.ws.chanels.new_account_virtual.NewAccountVirtual>`.
        """
        return NewAccountVirtual(self).__call__

    @property
    def oauth_apps(self):
        """Property for get Binary ws oauth_apps resource.

        :returns: The instance of :class:`OauthApps<binaryapi.ws.chanels.oauth_apps.OauthApps>`.
        """
        return OauthApps(self).__call__

    @property
    def p2p_advertiser_adverts(self):
        """Property for get Binary ws p2p_advertiser_adverts resource.

        :returns: The instance of :class:`P2PAdvertiserAdverts<binaryapi.ws.chanels.p2p_advertiser_adverts.P2PAdvertiserAdverts>`.
        """
        return P2PAdvertiserAdverts(self).__call__

    @property
    def p2p_advertiser_create(self):
        """Property for get Binary ws p2p_advertiser_create resource.

        :returns: The instance of :class:`P2PAdvertiserCreate<binaryapi.ws.chanels.p2p_advertiser_create.P2PAdvertiserCreate>`.
        """
        return P2PAdvertiserCreate(self).__call__

    @property
    def p2p_advertiser_info(self):
        """Property for get Binary ws p2p_advertiser_info resource.

        :returns: The instance of :class:`P2PAdvertiserInfo<binaryapi.ws.chanels.p2p_advertiser_info.P2PAdvertiserInfo>`.
        """
        return P2PAdvertiserInfo(self).__call__

    @property
    def p2p_advertiser_update(self):
        """Property for get Binary ws p2p_advertiser_update resource.

        :returns: The instance of :class:`P2PAdvertiserUpdate<binaryapi.ws.chanels.p2p_advertiser_update.P2PAdvertiserUpdate>`.
        """
        return P2PAdvertiserUpdate(self).__call__

    @property
    def p2p_advert_create(self):
        """Property for get Binary ws p2p_advert_create resource.

        :returns: The instance of :class:`P2PAdvertCreate<binaryapi.ws.chanels.p2p_advert_create.P2PAdvertCreate>`.
        """
        return P2PAdvertCreate(self).__call__

    @property
    def p2p_advert_info(self):
        """Property for get Binary ws p2p_advert_info resource.

        :returns: The instance of :class:`P2PAdvertInfo<binaryapi.ws.chanels.p2p_advert_info.P2PAdvertInfo>`.
        """
        return P2PAdvertInfo(self).__call__

    @property
    def p2p_advert_list(self):
        """Property for get Binary ws p2p_advert_list resource.

        :returns: The instance of :class:`P2PAdvertList<binaryapi.ws.chanels.p2p_advert_list.P2PAdvertList>`.
        """
        return P2PAdvertList(self).__call__

    @property
    def p2p_advert_update(self):
        """Property for get Binary ws p2p_advert_update resource.

        :returns: The instance of :class:`P2PAdvertUpdate<binaryapi.ws.chanels.p2p_advert_update.P2PAdvertUpdate>`.
        """
        return P2PAdvertUpdate(self).__call__

    @property
    def p2p_chat_create(self):
        """Property for get Binary ws p2p_chat_create resource.

        :returns: The instance of :class:`P2PChatCreate<binaryapi.ws.chanels.p2p_chat_create.P2PChatCreate>`.
        """
        return P2PChatCreate(self).__call__

    @property
    def p2p_order_cancel(self):
        """Property for get Binary ws p2p_order_cancel resource.

        :returns: The instance of :class:`P2POrderCancel<binaryapi.ws.chanels.p2p_order_cancel.P2POrderCancel>`.
        """
        return P2POrderCancel(self).__call__

    @property
    def p2p_order_confirm(self):
        """Property for get Binary ws p2p_order_confirm resource.

        :returns: The instance of :class:`P2POrderConfirm<binaryapi.ws.chanels.p2p_order_confirm.P2POrderConfirm>`.
        """
        return P2POrderConfirm(self).__call__

    @property
    def p2p_order_create(self):
        """Property for get Binary ws p2p_order_create resource.

        :returns: The instance of :class:`P2POrderCreate<binaryapi.ws.chanels.p2p_order_create.P2POrderCreate>`.
        """
        return P2POrderCreate(self).__call__

    @property
    def p2p_order_info(self):
        """Property for get Binary ws p2p_order_info resource.

        :returns: The instance of :class:`P2POrderInfo<binaryapi.ws.chanels.p2p_order_info.P2POrderInfo>`.
        """
        return P2POrderInfo(self).__call__

    @property
    def p2p_order_list(self):
        """Property for get Binary ws p2p_order_list resource.

        :returns: The instance of :class:`P2POrderList<binaryapi.ws.chanels.p2p_order_list.P2POrderList>`.
        """
        return P2POrderList(self).__call__

    @property
    def paymentagent_list(self):
        """Property for get Binary ws paymentagent_list resource.

        :returns: The instance of :class:`PaymentagentList<binaryapi.ws.chanels.paymentagent_list.PaymentagentList>`.
        """
        return PaymentagentList(self).__call__

    @property
    def paymentagent_transfer(self):
        """Property for get Binary ws paymentagent_transfer resource.

        :returns: The instance of :class:`PaymentagentTransfer<binaryapi.ws.chanels.paymentagent_transfer.PaymentagentTransfer>`.
        """
        return PaymentagentTransfer(self).__call__

    @property
    def paymentagent_withdraw(self):
        """Property for get Binary ws paymentagent_withdraw resource.

        :returns: The instance of :class:`PaymentagentWithdraw<binaryapi.ws.chanels.paymentagent_withdraw.PaymentagentWithdraw>`.
        """
        return PaymentagentWithdraw(self).__call__

    @property
    def payout_currencies(self):
        """Property for get Binary ws payout_currencies resource.

        :returns: The instance of :class:`PayoutCurrencies<binaryapi.ws.chanels.payout_currencies.PayoutCurrencies>`.
        """
        return PayoutCurrencies(self).__call__

    @property
    def ping(self):
        """Property for get Binary ws ping resource.

        :returns: The instance of :class:`Ping<binaryapi.ws.chanels.ping.Ping>`.
        """
        return Ping(self).__call__

    @property
    def portfolio(self):
        """Property for get Binary ws portfolio resource.

        :returns: The instance of :class:`Portfolio<binaryapi.ws.chanels.portfolio.Portfolio>`.
        """
        return Portfolio(self).__call__

    @property
    def profit_table(self):
        """Property for get Binary ws profit_table resource.

        :returns: The instance of :class:`ProfitTable<binaryapi.ws.chanels.profit_table.ProfitTable>`.
        """
        return ProfitTable(self).__call__

    @property
    def proposal(self):
        """Property for get Binary ws proposal resource.

        :returns: The instance of :class:`Proposal<binaryapi.ws.chanels.proposal.Proposal>`.
        """
        return Proposal(self).__call__

    @property
    def proposal_array(self):
        """Property for get Binary ws proposal_array resource.

        :returns: The instance of :class:`ProposalArray<binaryapi.ws.chanels.proposal_array.ProposalArray>`.
        """
        return ProposalArray(self).__call__

    @property
    def proposal_open_contract(self):
        """Property for get Binary ws proposal_open_contract resource.

        :returns: The instance of :class:`ProposalOpenContract<binaryapi.ws.chanels.proposal_open_contract.ProposalOpenContract>`.
        """
        return ProposalOpenContract(self).__call__

    @property
    def reality_check(self):
        """Property for get Binary ws reality_check resource.

        :returns: The instance of :class:`RealityCheck<binaryapi.ws.chanels.reality_check.RealityCheck>`.
        """
        return RealityCheck(self).__call__

    @property
    def residence_list(self):
        """Property for get Binary ws residence_list resource.

        :returns: The instance of :class:`ResidenceList<binaryapi.ws.chanels.residence_list.ResidenceList>`.
        """
        return ResidenceList(self).__call__

    @property
    def revoke_oauth_app(self):
        """Property for get Binary ws revoke_oauth_app resource.

        :returns: The instance of :class:`RevokeOauthApp<binaryapi.ws.chanels.revoke_oauth_app.RevokeOauthApp>`.
        """
        return RevokeOauthApp(self).__call__

    @property
    def sell(self):
        """Property for get Binary ws sell resource.

        :returns: The instance of :class:`Sell<binaryapi.ws.chanels.sell.Sell>`.
        """
        return Sell(self).__call__

    @property
    def sell_contract_for_multiple_accounts(self):
        """Property for get Binary ws sell_contract_for_multiple_accounts resource.

        :returns: The instance of :class:`SellContractForMultipleAccounts<binaryapi.ws.chanels.sell_contract_for_multiple_accounts.SellContractForMultipleAccounts>`.
        """
        return SellContractForMultipleAccounts(self).__call__

    @property
    def sell_expired(self):
        """Property for get Binary ws sell_expired resource.

        :returns: The instance of :class:`SellExpired<binaryapi.ws.chanels.sell_expired.SellExpired>`.
        """
        return SellExpired(self).__call__

    @property
    def set_account_currency(self):
        """Property for get Binary ws set_account_currency resource.

        :returns: The instance of :class:`SetAccountCurrency<binaryapi.ws.chanels.set_account_currency.SetAccountCurrency>`.
        """
        return SetAccountCurrency(self).__call__

    @property
    def set_financial_assessment(self):
        """Property for get Binary ws set_financial_assessment resource.

        :returns: The instance of :class:`SetFinancialAssessment<binaryapi.ws.chanels.set_financial_assessment.SetFinancialAssessment>`.
        """
        return SetFinancialAssessment(self).__call__

    @property
    def set_self_exclusion(self):
        """Property for get Binary ws set_self_exclusion resource.

        :returns: The instance of :class:`SetSelfExclusion<binaryapi.ws.chanels.set_self_exclusion.SetSelfExclusion>`.
        """
        return SetSelfExclusion(self).__call__

    @property
    def set_settings(self):
        """Property for get Binary ws set_settings resource.

        :returns: The instance of :class:`SetSettings<binaryapi.ws.chanels.set_settings.SetSettings>`.
        """
        return SetSettings(self).__call__

    @property
    def statement(self):
        """Property for get Binary ws statement resource.

        :returns: The instance of :class:`Statement<binaryapi.ws.chanels.statement.Statement>`.
        """
        return Statement(self).__call__

    @property
    def states_list(self):
        """Property for get Binary ws states_list resource.

        :returns: The instance of :class:`StatesList<binaryapi.ws.chanels.states_list.StatesList>`.
        """
        return StatesList(self).__call__

    @property
    def ticks(self):
        """Property for get Binary ws ticks resource.

        :returns: The instance of :class:`Ticks<binaryapi.ws.chanels.ticks.Ticks>`.
        """
        return Ticks(self).__call__

    @property
    def ticks_history(self):
        """Property for get Binary ws ticks_history resource.

        :returns: The instance of :class:`TicksHistory<binaryapi.ws.chanels.ticks_history.TicksHistory>`.
        """
        return TicksHistory(self).__call__

    @property
    def time(self):
        """Property for get Binary ws time resource.

        :returns: The instance of :class:`Time<binaryapi.ws.chanels.time.Time>`.
        """
        return Time(self).__call__

    @property
    def tnc_approval(self):
        """Property for get Binary ws tnc_approval resource.

        :returns: The instance of :class:`TncApproval<binaryapi.ws.chanels.tnc_approval.TncApproval>`.
        """
        return TncApproval(self).__call__

    @property
    def topup_virtual(self):
        """Property for get Binary ws topup_virtual resource.

        :returns: The instance of :class:`TopupVirtual<binaryapi.ws.chanels.topup_virtual.TopupVirtual>`.
        """
        return TopupVirtual(self).__call__

    @property
    def trading_durations(self):
        """Property for get Binary ws trading_durations resource.

        :returns: The instance of :class:`TradingDurations<binaryapi.ws.chanels.trading_durations.TradingDurations>`.
        """
        return TradingDurations(self).__call__

    @property
    def trading_times(self):
        """Property for get Binary ws trading_times resource.

        :returns: The instance of :class:`TradingTimes<binaryapi.ws.chanels.trading_times.TradingTimes>`.
        """
        return TradingTimes(self).__call__

    @property
    def transaction(self):
        """Property for get Binary ws transaction resource.

        :returns: The instance of :class:`Transaction<binaryapi.ws.chanels.transaction.Transaction>`.
        """
        return Transaction(self).__call__

    @property
    def transfer_between_accounts(self):
        """Property for get Binary ws transfer_between_accounts resource.

        :returns: The instance of :class:`TransferBetweenAccounts<binaryapi.ws.chanels.transfer_between_accounts.TransferBetweenAccounts>`.
        """
        return TransferBetweenAccounts(self).__call__

    @property
    def verify_email(self):
        """Property for get Binary ws verify_email resource.

        :returns: The instance of :class:`VerifyEmail<binaryapi.ws.chanels.verify_email.VerifyEmail>`.
        """
        return VerifyEmail(self).__call__

    @property
    def website_status(self):
        """Property for get Binary ws website_status resource.

        :returns: The instance of :class:`WebsiteStatus<binaryapi.ws.chanels.website_status.WebsiteStatus>`.
        """
        return WebsiteStatus(self).__call__
