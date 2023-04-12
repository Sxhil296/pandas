# pandas is used to analyze data
#Pandas is a Python library used for working with data sets.
#for analyzing, cleaning, exploring, and manipulating data.

import pandas as pd

# df = pd.read_csv('README.md')
#
# print(df.to_string())

myDataSet = {
    'cars': ["BMW", "Volvo", "Ford", "Tesla"],
    'passings': [3, 7, 2, 5]
}

myVar= pd.DataFrame(myDataSet)
print(myVar)

print(pd.__version__)