import pandas as pd

#increase the number of rows to display the entire df
# pd.options.display.max_rows = 9999

df = pd.read_csv("data.csv")
print(df) #doesn't return entire DataFrame
print()
print(df.to_string()) #returns entire DataFrame

#max rows
print(pd.options.display.max_rows)