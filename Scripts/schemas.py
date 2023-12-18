from google.cloud import bigquery

date_dimension_schema = [
    bigquery.SchemaField("date", "DATE", mode="REQUIRED"),
    bigquery.SchemaField("year", "INTEGER"),
    bigquery.SchemaField("month", "INTEGER"),
    bigquery.SchemaField("day", "INTEGER"),
]

ticker_dimension_schema = [
    bigquery.SchemaField("ticker", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("exchange", "STRING"),
    bigquery.SchemaField("sector", "STRING", mode="REQUIRED"),
]

fact_table_schema = [
    bigquery.SchemaField("date", "DATE", mode="REQUIRED"),
    bigquery.SchemaField("ticker", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("open", "FLOAT"),
    bigquery.SchemaField("close", "FLOAT"),
    bigquery.SchemaField("high", "FLOAT"),
    bigquery.SchemaField("low", "FLOAT"),
    bigquery.SchemaField("adj_close", "FLOAT"),
    bigquery.SchemaField("volume", "INTEGER"),
    bigquery.SchemaField("type", "STRING", mode="REQUIRED"),
]

correlation_table_schema = [
    bigquery.SchemaField("date","DATE"),
    bigquery.SchemaField("asset_a","STRING", mode="REQUIRED"),
    bigquery.SchemaField("asset_b","STRING", mode="REQUIRED"),
    bigquery.SchemaField("correlation","FLOAT"),
]

sector_dimension_schema = [
    bigquery.SchemaField("sector", "STRING", mode="REQUIRED"),
]

type_dimension_schema = [
    bigquery.SchemaField("type", "STRING", mode="REQUIRED"),
]

ema10_dimension_schema = [
    bigquery.SchemaField("date","DATE"),
    bigquery.SchemaField("ticker", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("moving_avg","INTEGER", mode="REQUIRED"),
]

ema50_dimension_schema = [
    bigquery.SchemaField("date","DATE"),
    bigquery.SchemaField("ticker", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("moving_avg","INTEGER", mode="REQUIRED"),
]

news_dimension_schema = [
    bigquery.SchemaField("date","DATE"),
    bigquery.SchemaField("ticker", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("text","STRING"),
    bigquery.SchemaField("sentiment","FLOAT"),
]