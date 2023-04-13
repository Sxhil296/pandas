import pandas as pd

# a = [1, 7, 3]
# myvar= pd.Series(a)
# print(myvar)


# seriesa is like a column in a table
# it is a 1D array holding data of any type
# 0 indexed, if nothing is specified, the values are labeled with their index numbers
# print(myvar[0])

# create lables
# myvar=pd.Series(a, index=['x', 'y', 'z'])
# print(myvar)
# print(myvar['y'])


# key/value objects as series
# the keys of the dictionary becomes the labels
calories = {'day1': 420, "day2": 380, "day3": 400}
myVar = pd.Series(calories)
print(myVar)



#DataFrames are multi-D tables
#while series is like a column, DataFrame is like a whole table

data = {
    "calories": [420, 380, 400],
    "duration": [50, 40, 45]
}
myCal=pd.DataFrame(data)
print(myCal)
