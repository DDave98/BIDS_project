from time import sleep
import config as cf
import data_download as dd
#import finviz_webscrap as fw
import big_query as bq


#bq.create_tables()
#bq.populate_dim_time()


for ticker in cf.tickers:
    #bq.populate_dim_ticker(dd.get_stock_detail(ticker))
    sanitized_stock_data = dd.get_stock_data(ticker)
    bq.upload_fact_stocks(sanitized_stock_data, ticker)
    sleep(8)
    #bq.populate_dim_news(fw.get_news_data(ticker)) # new added
    
    
