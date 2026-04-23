from moomoo import *

MOOMOOOPEND_ADDRESS = '127.0.0.1'  # mooomoo OpenD listening address
MOOMOOOPEND_PORT = 11111  # mooomoo OpenD listening port

TRADING_ENVIRONMENT = TrdEnv.SIMULATE  # Trading environment: REAL / SIMULATE
TRADING_MARKET = TrdMarket.US  # Transaction market authority, used to filter accounts
TRADING_PWD = 'xxxxx'  # Trading password, used to unlock trading for real trading environment
TRADING_PERIOD = KLType.K_1M  # Underlying trading time period
FAST_MOVING_AVERAGE = 1  # Parameter for fast moving average
SLOW_MOVING_AVERAGE = 3  # Parameter for slow moving average

WATCHLIST = ['US.SOFI', 'US.SNAP', 'US.PLTR',
    'US.ABAT', 'US.RR', 'US.OCGN']

# Unlock trade
# def unlock_trade():
#     if TRADING_ENVIRONMENT == TrdEnv.REAL:
#         ret, data = trd_ctx.unlock_trade(TRADING_PWD)
#         if ret != RET_OK:
#             print('Unlock trade failed: ', data)
#             return False
#         print('Unlock Trade success!')
#     return True


