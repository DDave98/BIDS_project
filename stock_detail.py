import pandas as pd
from yahooquery import Ticker

symbols = ['MSFT']

tickers = Ticker(symbols, asynchronous=True)

datasi = tickers.get_modules("summaryProfile quoteType")
print(datasi)