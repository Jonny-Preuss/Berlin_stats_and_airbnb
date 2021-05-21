import load_datasets
import pandas as pd

## changing the format of the date columns
df_c['date'] = pd.to_datetime(df_c['date'])
df_r['date'] = pd.to_datetime(df_r['date'])
df_rs['date'] = pd.to_datetime(df_rs['date'])
df_l['last_review'] = pd.to_datetime(df_l['last_review'])

## changing the last column in calendar dataset to float values, including stripping the $ sign
# needs to fill NA values for the strip method to work
df_c['price'] = df_c['price'].fillna("$0.00")
df_c['price'] = df_c['price'].apply(lambda x: x.strip("$"))
df_c['price'] = df_c['price'].apply(lambda x: x.replace(",",""))
df_c['price'] = df_c['price'].astype(float)
