from google.cloud import bigquery
import config as cf
import upload_to_bucket as gcs
import create_dates as cd
import schemas as sc

def create_bigquery_table(client,dataset_id,table_id, schema):
    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)

    table = bigquery.Table(table_temp,schema=schema)
    table = client.create_table(table)
    print(f'Table {table} has been created')

def load_into_table(gcs_uri, dataset_id, table_id):
    client = bigquery.Client()

    job_setting = bigquery.LoadJobConfig(
        autodetect=True, 
        write_disposition="WRITE_APPEND",
    )

    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)
    job = client.load_table_from_uri(
        gcs_uri,
        table_temp,
        job_config=job_setting
    )

    job.result()

    print(f'Job {job} has been finished')

def load_dim_ticker(gcs_uri, dataset_id, table_id):
    client = bigquery.Client()

    job_setting = bigquery.LoadJobConfig(
        autodetect=True, 
        write_disposition="WRITE_APPEND",
    )
    job_setting.schema = [
        bigquery.SchemaField("ticker", "STRING"),
        bigquery.SchemaField("exchange", "STRING"),
        bigquery.SchemaField("sector", "STRING"),
    ]
    job_setting.source_format = bigquery.SourceFormat.CSV

    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)

    job = client.load_table_from_uri(
        gcs_uri,
        table_temp,
        job_config=job_setting
    )

    job.result()

    print(f'Job {job} has been finished')

def load_dim_date(gcs_uri, dataset_id, table_id):
    client = bigquery.Client()

    job_setting = bigquery.LoadJobConfig(
        autodetect=True, 
        write_disposition="WRITE_APPEND",
    )
    job_setting.schema = [
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("day", "INTEGER"),
        bigquery.SchemaField("month", "INTEGER"),
        bigquery.SchemaField("year", "INTEGER"),
    ]
    job_setting.source_format = bigquery.SourceFormat.CSV

    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)

    job = client.load_table_from_uri(
        gcs_uri,
        table_temp,
        job_config=job_setting
    )

    job.result()

    print(f'Job {job} has been finished')

def create_tables():
    create_bigquery_table(cf.client,cf.dataset_name,cf.date_dim_table,sc.date_dimension_schema)
    create_bigquery_table(cf.client,cf.dataset_name,cf.ticker_dim_table,sc.ticker_dimension_schema)
    create_bigquery_table(cf.client,cf.dataset_name,cf.stock_fact_table,sc.fact_table_schema)

def populate_dim_ticker():
    gcs_url = gcs.upload_to_gcs2(cf.tickers_dim,cf.gcs_bucket_name,'dim_ticker.csv')
    load_dim_ticker(gcs_url,cf.dataset_name,cf.ticker_dim_table)

def populate_dim_time():
    dates = cd.create_dataframe(cf.start_date,cf.end_date)
    gcs_url = gcs.upload_to_gcs2(dates,cf.gcs_bucket_name,'dim_date.csv')
    load_dim_date(gcs_url,cf.dataset_name,cf.date_dim_table)

def upload_fact_stocks(sanitized_stock_data,ticker):
    gcs_fact_url = gcs.upload_to_gcs(sanitized_stock_data,cf.gcs_bucket_name,f'{ticker}_data.csv')
    load_into_table(gcs_fact_url,cf.dataset_name,cf.stock_fact_table)

def populate_dims():
    populate_dim_ticker()
    populate_dim_time()
