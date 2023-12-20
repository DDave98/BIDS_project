from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import random
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
        date = last_date

    # timestamp contain date = 'Today'
    elif timestamp[0] == 'Today':
        last_date = dt.datetime.now().date()
        last_date = last_date.strftime("%m/%d/%Y")
        date = last_date
    
    # timestamp contain date and time
    else:
        last_date = dt.datetime.strptime(timestamp[0], "%b-%d-%y") # from Dec-15-23
        last_date = last_date.strftime("%m/%d/%Y")        # to 2023-12-15
        last_date = str(last_date)
        date = last_date
    return date

def fake_date(index):
    fake = dt.datetime.today() - dt.timedelta(days=index)
    fake = fake.strftime("%m/%d/%Y")
    return str(fake)

def fake_compaund(compaund):
    if compaund == 0.0:
        return float(compaund + random.random())
    else:
        return float(compaund)

def parse_news_data(html:str, ticker:str):
    data_table = html.find(id='news-table')
    table_rows = data_table.findAll('tr')
    news_data = [] # collect of all records
    vader = SIA()  # text compaund analyser

    for index, row in enumerate(table_rows):
        record = {
            'ticker': ticker,
            'text': row.a.text,
            'compound': fake_compaund(vader.polarity_scores(row.a.text)['compound']),
            'source': (row.span.text)[1:-1],
            'url': row.a['href'],
            'date': fake_date(index),#parse_timestamp(row.td.text),
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
    return df

get_news_data(cf.tickers[9])