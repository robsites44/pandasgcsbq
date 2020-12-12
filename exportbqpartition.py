import pandas as pd
from google.cloud import bigquery

bq_client = bigquery.Client(project='<project>')

load_job = bq_client.load_table_from_dataframe(
    df, '<project>.<dataset>.<table>$20201018'
)

result = load_job.result()
