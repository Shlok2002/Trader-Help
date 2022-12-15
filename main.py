from kite_trade import *

enctoken = "3U0hTDnfrF09pSCth+LI9HcLcaMKAFP4QTQb7r77Blz8dJVc8aJKo22F9h5uG4doSr/l4KGIymQFq4TQeHoOIG3mJNOu4N86DiQl/9fJYLScDTMRbLwSzg=="
kite = KiteApp(enctoken=enctoken)


order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="TRACXN",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=5,
                         product=kite.PRODUCT_CNC,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="TradeViaPython")
print(order)