from connect_db import Client as db
from operations_lib import DefaultOperations as ops
from data_objects import Dataset as ds
from data_objects import Table as tb
import pandas as pd

from download_data import FinanceDownloader
from download_data import EventDowloader

#create client for specific dataset and table
stock_client = db(ds.STOCKS,tb.STOCK_DATA_LIVE)
forex_client = db(ds.FOREX,tb.FOREX_DATA_LIVE)
DBclient = db(ds.NEWS, tb.NEWS)

"""
call functions from DefaultOperations using client created above
data can be printed directly or in cycle if more than 1 result is present
"""
def print_schema():
    #get schema of table
    stock_schema = ops.get_schema(stock_client.table)
    print(stock_schema)

    news_schema = ops.get_schema(DBclient.table)
    print(news_schema)

def Insert_finance_data():
    fd = FinanceDownloader(save=True)
    fd.download_data("MSFT", "1990-01-01", "2000-01-01")
    source= pd.read_csv("./data/data_MSFT.csv")

    for index, row in source.iterrows():
        data = ops.insert_data(stock_client.client, stock_client.table, ['MSFT', row[1], row[4], row[2], row[3], row[-1], row[-2], row[0]])
        #print(data)

def Insert_event_data():
    pass

# INSERT Finance DATA INTO DB

# INSERT Event DATA INTO DB

# CREATE DIM TABLES (time, events, ticker, type, exchange, sector)
 