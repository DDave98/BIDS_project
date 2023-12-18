from time import sleep
import yfinance as yf
from polygon import RESTClient
import json 
import pandas as pd
import config as cf

def download_stock_data(ticker:str, start_date:str, end_date:str) -> pd.DataFrame:
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    print(f'Data about {ticker} has been downloaded')
    return stock_data

def sanitize_stock_data(stock_data:pd.DataFrame,ticker) -> pd.DataFrame:
    stock_data = stock_data.resample('D').ffill()
    stock_data = stock_data.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume'
    })
    stock_data['ticker'] = ticker
    print(f'Data has been sanitized')
    return stock_data

def get_stock_data(ticker):
    stock_data = download_stock_data(ticker,cf.start_date,cf.end_date)
    sanitized_stock_data = sanitize_stock_data(stock_data,ticker)
    return sanitized_stock_data

def get_stock_detail(ticker):
    client = RESTClient(api_key="VNVFhfaQwBpSL9X1dOre_leLPN2XnBCW")
    data = client.get_ticker_details(ticker)
    print(data.ticker,data.locale,data.sic_description)
    sleep(18)
    return pd.DataFrame({
        "ticker":[data.ticker],
        "exchange":[data.locale],
        "sector":[data.sic_description]
        })
    
