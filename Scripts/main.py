from connect_db import Client as db
from operations_lib import DefaultOperations as ops
from data_objects import Dataset as ds
from data_objects import Table as tb
import pandas as pd

from download_data import FinanceDownloader
from download_data import EventDowloader

from config import FinanceDataDownloadParams

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
    news_schema = ops.get_schema(DBclient.table)

    print('\n'.join(map(str, stock_schema)))
    #print(news_schema)

def Get_finance_data():
    fd = FinanceDownloader(save=True)
    fd.get_dict(FinanceDataDownloadParams.types, FinanceDataDownloadParams.start, FinanceDataDownloadParams.end)
    source = pd.DataFrame() # empty pandas dataframe

    # make one dataframe for all ticker -> read csv and add to source
    for fileName in FinanceDataDownloadParams.types:
        fileSource = pd.read_csv(f"./data/data_{fileName}.csv", sep=",", header=0)
        fileSource["ticker"] = fileName # add ticker name 
        fileSource = fileSource.iloc[:, [7, 1, 4, 2, 3, 6, 5, 0]] # reorder column
        source = pd.concat([source, fileSource], ignore_index=True)

    return source;

def Insert_finance_data(source):
    for index, row in source.iterrows():
        data = ops.insert_data(stock_client.client, stock_client.table, row.to_numpy())

def Insert_event_data():
    pass

######################################################
print_schema()

# INSERT Finance DATA INTO DB
finance_data = Get_finance_data();
print(finance_data)
#Insert_finance_data(finance_data)

# INSERT Event DATA INTO DB

# CREATE DIM TABLES (time, events, ticker, type, exchange, sector)
 