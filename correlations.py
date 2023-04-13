# corr() calculates the relationship between each column in your data set

import pandas as pd
df = pd.read_csv('data2.csv')

print(df.corr())