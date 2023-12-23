from google.cloud import storage
from io import BytesIO
import pandas as pd

def upload_to_gcs_with_header(data:pd.DataFrame,bucket_name:str,blob_name:str) -> str:
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    csv_data = data.to_csv(header=True)
    csv_bytes = BytesIO(csv_data.encode('utf-8'))

    blob = bucket.blob(blob_name)
    blob.upload_from_file(csv_bytes,content_type='text/csv')

    blob_url = f'gs://{bucket_name}/{blob_name}'

    print(f'Blob {blob_url} has been created')

    return blob_url

def upload_to_gcs_no_header(data:pd.DataFrame,bucket_name:str,blob_name:str) -> str:
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    csv_data = data.to_csv(header=False, index=False)
    csv_bytes = BytesIO(csv_data.encode('utf-8'))

    blob = bucket.blob(blob_name)
    blob.upload_from_file(csv_bytes,content_type='text/csv')

    blob_url = f'gs://{bucket_name}/{blob_name}'

    print(f'Blob {blob_url} has been created')

    return blob_url