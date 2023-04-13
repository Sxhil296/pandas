#head() returns the headers and a specified number of rows, starting from the top, default is 5 rows
#tail() method is used to view rows from the last

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
print(df.tail(10))

#info()
print()
print(df.info())