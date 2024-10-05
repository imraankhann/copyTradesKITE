from kite_trade import *

# # First Way to Login
# # You can use your Kite app in mobile
# # But You can't login anywhere in 'kite.zerodha.com' website else this session will disconnected

# user_id = "IG8705"       # Login Id
# password = "***@"      # Login password
# twofa = "081718"         # Login Pin or TOTP

# enctoken = get_enctoken(user_id, password, twofa)
# kite = KiteApp(enctoken=enctoken)

# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

enctoken = ""
kite = KiteApp(enctoken=enctoken)

# Basic calls
print(kite.profile())
print(kite.margins())
print(kite.orders())

print("================ PRINT INSTRUMENTS =======================")

# Get instrument or exchange
#print(kite.instruments())
print(kite.instruments("NSE_INDEX|Nifty 50"))
# print(kite.instruments("NFO"))
#instrument_dump = kite.instruments(exchange='NSE')
#print("Instrument Token : ", instrument_dump)

print("================= PRINT LTP AND QUOTE ============")
#print(kite.ltp("NSE:RELIANCE"))
# print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
# print(kite.quote(["NSE: NIFTY BANK", "NSE:ACC", "NSE:NIFTY24500PE"]))

#print("=================== GET TICKER ID =================")

# Get Tick Data 'Use Websocket'
# from kiteconnect import KiteTicker
# user_id = kite.profile()["user_id"]
# kws = KiteTicker(api_key="TradeViaPython", access_token=enctoken+"&user_id="+user_id)

print("============ GET HISTORICAL DATA ====================")
import datetime
instrument_token = 256265
from_datetime = datetime.datetime.now() - datetime.timedelta(days=2)     # From last & days
to_datetime = datetime.datetime.now()
interval = "60minute"
print(kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False))

# Place Order
# #order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                          exchange=kite.EXCHANGE_NSE,
#                          tradingsymbol="GAIL",
#                          transaction_type=kite.TRANSACTION_TYPE_BUY,
#                          quantity=1,
#                          product=kite.PRODUCT_MIS,
#                          order_type=kite.ORDER_TYPE_MARKET,
#                          price=None,
#                          validity=None,
#                          disclosed_quantity=None,
#                          trigger_price=None,
#                          squareoff=None,
#                          stoploss=None,
#                          trailing_stoploss=None,
#                          tag="TradeLike_iKhan")
# print(order)

# Modify order
# kite.modify_order(variety=kite.VARIETY_REGULAR,
#                   order_id="order_id",
#                   parent_order_id=None,
#                   quantity=5,
#                   price=200,
#                   order_type=kite.ORDER_TYPE_LIMIT,
#                   trigger_price=None,
#                   validity=kite.VALIDITY_DAY,
#                   disclosed_quantity=None)

# Cancel order
# kite.cancel_order(variety=kite.VARIETY_REGULAR,
#                   order_id="order_id",
#                   parent_order_id=None)