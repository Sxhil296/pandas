import pandas as pd

data = {
    "fnmae": ["Sahil", "Faraj", "Aasim"],
    "lname": ["Malik", "Ali", "Syed"]
}

df = pd.DataFrame(data, index = [1, 2, 3])
print(df)

# locate row
# print()
#
# print(df.loc[0])  # returns a series
# print()
# print(df.loc[[0, 1]])  # returns a dataframe

#locate named indexes
print()
print(df.loc[2])
print()

#load files into dataframe
dff=pd.read_csv('README.md')
print(dff)