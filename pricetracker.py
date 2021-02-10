import yfinance as yf
from cls import cls

def pricetracker(stock):
    while True:
        tickerdata = yf.Ticker(stock)
        tickerinfo = tickerdata.info
        cls()
        print(tickerinfo.get("symbol") + " " + tickerinfo.get('shortName') + " " + str(tickerinfo.get('regularMarketPrice')))
#not finished