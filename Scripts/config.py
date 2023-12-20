from google.cloud import bigquery
import pandas as pd

gcs_bucket_name = 'ingest_bucket_xpech_michalica'
dataset_name = 'xpech_michalica'
date_dim_table = 'dim_date'
ticker_dim_table = 'dim_ticker'
stock_fact_table = 'stocks_v2'
news_dim_table = 'dim_news'

client = bigquery.Client()

tickers = [
    'AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'ALL', 'AMGN', 'AMT', 'AMZN',
    'AXP', 'BA', 'BAC', 'BIIB', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK.B', 'C',
    'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS',
    'CVX', 'DD', 'DHR', 'DIS', 'DOW', 'DUK', 'EMR', 'EXC', 'F', 'FB', 'FDX',
    'GD', 'GE', 'GILD', 'GM', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC',
    'JNJ', 'JPM', 'KHC', 'KMI', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD',
    'MDLZ', 'MDT', 'MET', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX',
    'NKE', 'NVDA', 'ORCL', 'OXY', 'PEP', 'PFE', 'PG', 'PM', 'PYPL', 'QCOM',
    'RTX', 'SBUX', 'SLB', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TSLA', 'TXN',
    'UNH', 'UNP', 'UPS', 'USB', 'V', 'VZ', 'WBA', 'WFC', 'WM', 'XOM',
    'BABA', 'TCEHY', 'PTR', 'BHP', 'TM', 'RIO', 'NVO', 'ASML', 'LVMUY',
    'SAP', 'ING', 'TOT', 'RY', 'SNE', 'NVS', 'TMUS', 'TSM', 'RYAAY', 'BP',
    'UL', 'AZN', 'SAN', 'BNS', 'ING', 'MTU', 'UBS', 'CS', 'BBD', 'CHL',
    'PTR', 'TSM', 'TOT', 'SNY', 'BTI', 'BP', 'UN', 'UL', 'BHP', 'RIO'
]
start_date = '2023-01-01'
end_date = '2023-01-31'

def write_append():
    return bigquery.LoadJobConfig(
        autodetect=True, 
        write_disposition="WRITE_APPEND",
    )