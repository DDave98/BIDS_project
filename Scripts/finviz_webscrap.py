from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import config as cf

finviz_url = 'https://finviz.com/quote.ashx?t='
last_date = '0000-00-00' # last date used in records

import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def parse_timestamp(html_timestamp):
    # clear timestamp and split into list
    timestamp = list(filter(None, html_timestamp.replace('\r\n', '').split(' ')))
    date = ''
    global last_date

    # timestamp contain only time
    if len(timestamp) == 1:
        date = last_date + " " + timestamp[0]

    # timestamp contain date = 'Today'
    elif timestamp[0] == 'Today':
        last_date = str(dt.datetime.now().date())
        date = last_date + " " + timestamp[1]
    
    # timestamp contain date and time
    else:
        last_date = dt.datetime.strptime(timestamp[0], "%b-%d-%y") # from Dec-15-23
        last_date = last_date.strftime("%Y-%m-%d")        # to 2023-12-15
        last_date = str(last_date)
        date = last_date + " " + timestamp[1]
    
    return date

def parse_news_data(html:str, ticker:str):
    data_table = html.find(id='news-table')
    table_rows = data_table.findAll('tr')
    news_data = [] # collect of all records
    vader = SIA()  # text compaund analyser

    for index, row in enumerate(table_rows):
        record = {
            'ticker': ticker,
            'date': parse_timestamp(row.td.text),
            'title': row.a.text,
            'source': (row.span.text)[1:-1],
            'url': row.a['href'],
            'compound': vader.polarity_scores(row.a.text)['compound']
        }

        #print(timestamp,record,'\n')
        news_data.append(record)
    
    return news_data

def dowload_news_data(ticker:str):
    url = finviz_url + ticker
    reqest = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(reqest)
    html = BeautifulSoup(response, 'html')
    return html

def get_news_data(ticker):
    web_page = dowload_news_data(ticker)
    news_data = parse_news_data(web_page, ticker)

    df = pd.DataFrame(news_data)    
    print(df)

get_news_data(cf.tickers[9])