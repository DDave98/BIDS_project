from connect_db import Client as db
from operations_lib import DefaultOperations as ops
from data_objects import Dataset as ds
from data_objects import Table as tb


#create client for specific dataset and table
stock_client = db(ds.STOCKS,tb.STOCK_DATA_LIVE)
forex_client = db(ds.FOREX,tb.FOREX_DATA_LIVE)

"""
call functions from DefaultOperations using client created above
data can be printed directly or in cycle if more than 1 result is present
"""
#get schema of table
stock_schema = ops.get_schema(stock_client.table)
print(stock_schema)

forex_schema = ops.get_schema(forex_client.table)
print(forex_schema)

#select * from table
data = ops.get_data(stock_client.client,stock_client.table)

#query data
data = ops.query(
    client = stock_client.client,
    i_query = f"SELECT * FROM {stock_client.table}"
    )
