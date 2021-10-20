# noinspection PyPep8Naming
class PROPOSAL_BASIS:
    STAKE = "stake"
    PAYOUT = "payout"


# noinspection PyPep8Naming
class DURATION:
    DAY = "d"
    MINUTE = "m"
    SECOND = "s"
    HOUR = "h"
    TICK = "t"

    D = DAY
    M = MINUTE
    S = SECOND
    H = HOUR
    T = TICK


# noinspection PyPep8Naming,SpellCheckingInspection
class CONTRACT_TYPE:
    MULTUP = "MULTUP"
    MULTDOWN = "MULTDOWN"
    UPORDOWN = "UPORDOWN"
    EXPIRYRANGE = "EXPIRYRANGE"
    ONETOUCH = "ONETOUCH"
    CALLE = "CALLE"
    LBHIGHLOW = "LBHIGHLOW"
    ASIAND = "ASIAND"
    EXPIRYRANGEE = "EXPIRYRANGEE"
    DIGITDIFF = "DIGITDIFF"
    DIGITMATCH = "DIGITMATCH"
    DIGITOVER = "DIGITOVER"
    PUTE = "PUTE"
    DIGITUNDER = "DIGITUNDER"
    NOTOUCH = "NOTOUCH"
    CALL = "CALL"
    RANGE = "RANGE"
    LBFLOATPUT = "LBFLOATPUT"
    DIGITODD = "DIGITODD"
    PUT = "PUT"
    ASIANU = "ASIANU"
    LBFLOATCALL = "LBFLOATCALL"
    EXPIRYMISSE = "EXPIRYMISSE"
    EXPIRYMISS = "EXPIRYMISS"
    DIGITEVEN = "DIGITEVEN"
    TICKHIGH = "TICKHIGH"
    TICKLOW = "TICKLOW"
    RESETCALL = "RESETCALL"
    RESETPUT = "RESETPUT"
    CALLSPREAD = "CALLSPREAD"
    PUTSPREAD = "PUTSPREAD"
    RUNHIGH = "RUNHIGH"
    RUNLOW = "RUNLOW"


# noinspection PyPep8Naming
class MSG_TYPE:
    AUTHORIZE = 'authorize'
    BALANCE = 'balance'
    TICK = 'tick'  # response
    TICKS = 'ticks'  # request
    BUY = 'buy'
    PROPOSAL = 'proposal'
    ASSET_INDEX = 'asset_index'
    FORGET = 'forget'
    FORGET_ALL = 'forget_all'

# class BUY_RESPONSE:
#     BUY_REQUEST: bool
#     def __init__(self):
#         self.BUY_REQUEST = False
#         self.PROPOSAL_REQUEST = False
#         self.CONTRACT_ID = None
#         self.BUY_REQ_ID = None
#         self.PROPOSAL_REQ_ID = None
