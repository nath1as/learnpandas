import pandas as pd

df = pd.read_csv('ZILLOW-C.csv')
df.set_index('Date', inplace = True)
print(df.head())

