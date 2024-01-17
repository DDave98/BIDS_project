from google.cloud import bigquery
import config as cf
import upload_to_bucket as gcs
import create_dates as cd
import data_download as dd
import schemas as sc

def create_bigquery_table(client,dataset_id,table_id, schema):
    #Create references to dataset/table
    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)
    table = bigquery.Table(table_temp,schema=schema)
    if table_id == "assets":
        table.time_partitioning = bigquery.TimePartitioning(
            type_= bigquery.TimePartitioningType.MONTH,
            field="date"
        )
        table.clustering_fields = ["ticker"]
    #Create table
    table = client.create_table(table)
    print(f'Table {table} has been created')

def load_into_table(gcs_uri, dataset_id, table_id):
    #Create references
    client = bigquery.Client()
    dataset_temp = client.dataset(dataset_id)
    table_temp = dataset_temp.table(table_id)

    #Setup job
    job_setting = cf.write_append()
    job = client.load_table_from_uri(
        gcs_uri,
        table_temp,
        job_config=job_setting
    )

    job.result()

    print(f'Job {job} has been finished')

def load_dim_ticker(gcs_uri, dataset_id, table_id):
    client = bigquery.Client()

    job_setting = cf.write_append()
    job_setting.schema = sc.ticker_dimension_schema
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

def load_dim_news(gcs_uri, dataset_id, table_id):
    client = bigquery.Client()

    job_setting = cf.write_append()
    job_setting.schema = sc.news_dimension_schema
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
    job_setting.schema = sc.date_dimension_schema
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
    #create_bigquery_table(cf.client,cf.dataset_name,cf.date_dim_table,sc.date_dimension_schema)         # dim table - date 
    #create_bigquery_table(cf.client,cf.dataset_name,cf.ticker_dim_table,sc.ticker_dimension_schema)     # dim table - ticker
    #create_bigquery_table(cf.client,cf.dataset_name,cf.news_dim_table,sc.news_dimension_schema)         # dim table - news
    create_bigquery_table(cf.client,cf.dataset_name,cf.stock_fact_table,sc.fact_table_schema)           # fac table - stock

def populate_dim_ticker(data):
    name = f'dim_ticker_{data["ticker"][0]}.csv'
    gcs_url = gcs.upload_to_gcs_no_header(data,cf.gcs_bucket_name,name)
    load_dim_ticker(gcs_url,cf.dataset_name,cf.ticker_dim_table)

def populate_dim_time():
    dates = cd.create_dataframe(cf.start_date,cf.end_date)
    gcs_url = gcs.upload_to_gcs_no_header(dates,cf.gcs_bucket_name,'dim_date.csv')
    load_dim_date(gcs_url,cf.dataset_name,cf.date_dim_table)

def upload_fact_stocks(sanitized_stock_data,ticker):
    gcs_fact_url = gcs.upload_to_gcs_with_header(sanitized_stock_data,cf.gcs_bucket_name,f'{ticker}_data.csv')
    load_into_table(gcs_fact_url,cf.dataset_name,cf.stock_fact_table)

def populate_dim_news(data):
    name = f'dim_news.csv'
    gcs_url = gcs.upload_to_gcs_no_header(data,cf.gcs_bucket_name,name)
    load_dim_news(gcs_url,cf.dataset_name,cf.news_dim_table)

