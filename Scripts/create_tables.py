from google.cloud import bigquery as bq
from config import client, dataset_name
from schemas import fact_table_schema


table = bq.Table("bids-xpech-michalica."+dataset_name+".test_table",fact_table_schema)
table.clustering_fields = ["ticker","type"]
table.time_partitioning = bq.TimePartitioning(
    type_=bq.TimePartitioningType.DAY,
    field = "date",
    expiration_ms=1000 * 60 * 60 * 24 * 90
)
table = client.create_table(table)
