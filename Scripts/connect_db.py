from google.cloud import bigquery

class Client():
    table: bigquery.Table
    dataset_id: str
    table_id: str
    project_id: str
    client: bigquery.Client

    # Reference the table
    def setup_reference(self):
            table_ref = self.client.dataset(self.dataset_id, project=self.project_id).table(self.table_id)
            self.table = self.client.get_table(table_ref)

    def __init__(self, dataset_id, table_id):
        self.client = bigquery.Client()

        #project_id is always static/same
        self.project_id = "imperial-sensor-400812"

        #has to be changed base on dataset and table we work on
        self.dataset_id = dataset_id
        self.table_id = table_id

        self.setup_reference()
    
