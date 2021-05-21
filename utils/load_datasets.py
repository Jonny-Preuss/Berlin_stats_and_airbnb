import pandas as pd

path = 'drive/MyDrive/Colab Notebooks/BI/data/'


df_cr = pd.read_csv(path+'Berlin_crimes.csv', encoding="utf-8", parse_dates=['Year'])
df_n = pd.read_csv(path+'berlin_neighbourhoods.csv', encoding="utf-8")
df_c = pd.read_csv(path+'calendar_summary.csv', encoding="utf-8")
df_r = pd.read_csv(path+'reviews.csv', encoding="utf-8")
df_rs = pd.read_csv(path+'reviews_summary.csv', encoding="utf-8")
df_l = pd.read_csv(path+'listings.csv', encoding="utf-8")
df_ls = pd.read_csv(path+'listings_summary.csv', encoding="utf-8")
