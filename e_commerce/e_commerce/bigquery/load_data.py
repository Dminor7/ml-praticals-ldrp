from google.cloud import bigquery

class BigQuery:
    def __init__(self, service_account_path: str) -> None:
        self.service_account_path = service_account_path
        self.client = bigquery.Client.from_service_account_json(self.service_account_path)
    
    def get_data(self, query):
        job_id = self.client.query(query=query)
        job_id.result()
        return job_id.to_dataframe()

