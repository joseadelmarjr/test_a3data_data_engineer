from google.cloud import bigquery
import pandas as pd


class BigQueryConnector:
    def __init__(self, project_id):
        self.client = bigquery.Client(project=project_id)

    def run_query(self, query):
        try:
            query_job = self.client.query(query)
            results = query_job.result()
            df = results.to_dataframe()
            return df
        except Exception as e:
            print("Something was wrong.")
            print(e)

    def save_dataframe(self, dataframe, table_name, dataset_name):
        dataset_ref = self.client.dataset(dataset_name)
        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig(
            schema=[],
            write_disposition="WRITE_TRUNCATE",
        )

        job = self.client.load_table_from_dataframe(
            dataframe, table_ref, job_config=job_config
        )
        job.result()
