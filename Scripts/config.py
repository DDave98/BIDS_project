from google.cloud import bigquery
import pandas as pd

gcs_bucket_name = 'ingest_bucket_xpech_michalica'
dataset_name = 'xpech_michalica'
date_dim_table = 'dim_date'
ticker_dim_table = 'dim_ticker'
stock_fact_table = 'stocks_v2'

client = bigquery.Client()

##DATA##
###################################################################################################
#needs some stronger setup
tickers = ['AAPL','MSFT']
start_date = '2023-01-01'
end_date = '2023-01-31'


#to be downloaded from yahoofinance API
tickers_dim = pd.DataFrame({
    'ticker':['AAPL'],
    'exchange':['NASDAQ'],
    'sector':['technology'],
}) 
###################################################################################################
