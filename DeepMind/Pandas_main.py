import pandas as pd
import numpy as np

#Pandas seris is one-dimensional labeled array 
#capable of holding data of any type
s = pd.Series()
print("Pandas Series: ", s)

data = np.array(['G','P','U'])
s = pd.Series(data)
print("s:\n", s)

#Pandas DataFrame is a two-dimensional data structure
#works with lists, dictionaries
df = pd.DataFrame()
print(df)

lst = ["google", "meta", "amazondotcom", "nvidia", "micro-soft", "apple"]
df = pd.DataFrame(lst)
print(df)


data = [
    {'name':'Riya', 'age':'25', 'city': 'NYU'}, 
    {'name':'Suzuki', 'age':'23', 'city': 'Tokio'},
    {'name':'Elizabeth', 'age':'26', 'city': 'London'},
    {'name':'Sam', 'age':'30', 'city': 'SanFrancisco'}, 
    {'name':'Bob', 'age':'28', 'city': 'Boston'},
    {'name':'Ashe', 'age':'26', 'city': 'Zurich'}
    ]
df = pd.DataFrame(data)

df.to_csv("data.csv", index=False) #creates the data.csv
df = pd.read_csv("data.csv")

sorted_column = df.sort_values(['name'], ascending=False)
print(sorted_column, end="\n")
print("First 5 rows:", df.head(), end="\n") 
print("Last 5 rows:", df.tail(), end="\n")
print("Mean of ages:", df['age'].mean(), end="\n")

#viewing and exploring data!
print(df.info())

#handling missing data
print(df.isnull().sum())
df = df.fillna(0) #replaces missing values with 0

#selecting and filtering data
ages = df[df['age']>25]
print(ages, end="\n")

#adding and removing columns not rows!
df['total'] = df['age']
print(df.head(), end="\n")
print(df.shape) #(6,4)


#grouping data(groupby)
res = df.groupby('name')['age'].sum()
print(res, end="\n")

newData = pd.DataFrame.join(pd.DataFrame(lst), df)
print("Companies-persons-info:\n", newData)