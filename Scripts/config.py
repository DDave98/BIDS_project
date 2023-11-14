from google.cloud import bigquery
import pandas as pd

gcs_bucket_name = 'ingest_bucket_xpech_michalica'
dataset_name = 'xpech_michalica'
date_dim_table = 'dim_date'
ticker_dim_table = 'dim_ticker'
stock_fact_table = 'stocks_v2'

client = bigquery.Client()

##SCHEMAS##
###################################################################################################
date_dimension_schema = [
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("year", "INTEGER"),
    bigquery.SchemaField("month", "INTEGER"),
    bigquery.SchemaField("day", "INTEGER"),
]

ticker_dimension_schema = [
    bigquery.SchemaField("ticker", "STRING"),
    bigquery.SchemaField("exchange", "STRING"),
    bigquery.SchemaField("sector", "STRING"),
]

fact_table_schema = [
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("ticker", "STRING"),
    bigquery.SchemaField("open", "FLOAT"),
    bigquery.SchemaField("close", "FLOAT"),
    bigquery.SchemaField("high", "FLOAT"),
    bigquery.SchemaField("low", "FLOAT"),
    bigquery.SchemaField("adj_close", "FLOAT"),
    bigquery.SchemaField("volume", "INTEGER"),
]
###################################################################################################



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
