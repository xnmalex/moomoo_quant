from moomoo import *
from config import *

class MoomooClient:
    def __enter__(self):
        self.quote_ctx = OpenQuoteContext(host=MOOMOOOPEND_ADDRESS, port=MOOMOOOPEND_PORT)
        self.trade_ctx = OpenSecTradeContext(filter_trdmarket=TRADING_MARKET, host=MOOMOOOPEND_ADDRESS, port=MOOMOOOPEND_PORT, security_firm=SecurityFirm.FUTUSECURITIES)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quote_ctx.close()
        self.trade_ctx.close()