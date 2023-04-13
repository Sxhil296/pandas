#data cleaning means fixing bad data in your data set
#bad data = empty cells, data in wrong format, wrong data, duplicates

import pandas as pd

df = pd.read_csv('data.csv')
#remove rows
new_df = df.dropna() #dropna() method doesn't change the original df, it returns a new df
# df.dropna(inplace = True) to change the original df
print(new_df.to_string())


#fillna() - replace empty values
# df = pd.read_csv('data.csv')
#
# df.fillna(130, inplace = True)

# convert data into correct format
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())


#replacing values
# df.loc[7, 'Duration'] = 45

#finding duplicates
print(df.duplicated())
#removing duplicates
df.drop_duplicates(inplace=True)