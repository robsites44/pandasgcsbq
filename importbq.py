import pandas as pd 

df = pd.read_gbq('SELECT repository.url, repository.created_at,repository.size FROM `bigquery-public-data.samples.github_nested` LIMIT 1000')
df.head(5)