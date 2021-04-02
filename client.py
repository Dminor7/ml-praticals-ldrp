from e_commerce.bigquery import BigQuery

df = BigQuery("./service-account.json").get_data("query")
print(df.head())
