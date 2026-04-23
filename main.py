from strategy import premarket_scan
from moomoo_client import MoomooClient
from config import WATCHLIST
from moomoo import RET_OK

def run():
    with MoomooClient() as client:
        try:
        
            ret, data = client.quote_ctx.get_market_snapshot(WATCHLIST)
            
            if ret == RET_OK:
                # print(data)
                print(premarket_scan(data))
            else:
                print('error:', data)
                 
        except Exception as e:
            print(f"error {e}")

        finally:
            client.quote_ctx.close()
            client.trade_ctx.close()


if __name__ == "__main__":
    run()