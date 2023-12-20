import config as cf
import data_download as dd
import finviz_webscrap as fw
import big_query as bq


#bq.create_tables()
#CREATE DOWNLOADER FOR TICKER DIM -- CURENTLY HARDCODED IN CONFIG


for ticker in cf.tickers:
    #sanitized_stock_data = dd.get_stock_data(ticker)
    #bq.upload_fact_stocks(sanitized_stock_data, ticker)
    #bq.populate_dim_ticker(dd.get_stock_detail(ticker))
    bq.populate_dim_news(fw.get_news_data(ticker)) # new added
    
