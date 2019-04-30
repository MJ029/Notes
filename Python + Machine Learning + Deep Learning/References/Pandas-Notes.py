import numpy as np
import pandas as pd

######### Pandas Series #########
# by parsing list
a = pd.Series([1, 2, 3, 4, np.nan, 6, 7])
print(a)

# by parsing ndArray
ser_arr = np.array([3] * 4, dtype=np.int32)
b = pd.Series(ser_arr)


######## Creating a DataFrame ########
# by passing a NumPy array
df = pd.DataFrame(np.random.rand(6, 4), columns=list('ABCD'))
print(df)

# by passing a NumPy array With Custom Index
dates = pd.date_range('20190304', periods=6)
df1 = pd.DataFrame(np.random.rand(6, 5), index=dates, columns=['A','B','C','D','E'])
print(df1)

# by parsing dist object
dist_obj = {'A': 1,
            'B': pd.date_range('20190304', periods=4),
            'C': pd.Series(1, index = list(range(4)), dtype=np.float64),
            'D': np.array([3] * 4, dtype=np.int32),
            'E': pd.Categorical(['test', 'train', 'test', 'train']),
            'F': 'Y'}
df2 = pd.DataFrame(dist_obj)


######## DataFrame attributes operation ########
#to check datatypes of dataframe
print(df.dtypes)
print(df1.dtypes)
print(df2.dtypes)

#AutoFill
#df2.<TAB>
df2.B

#To take rowIndex information
df.index
df1.index
df2.index

# To take column information
df.columns
df1.columns
df2.columns

# Describe Df
df.describe()
df1.describe()
df2.describe()

# Dataframe Pivot
df.T
df1.T
df2.T

# To sort by Axis
df.sort_index(axis=1, ascending=False)

# To sort by value
df1.sort_values(by='B')


######## DataFrame Select operation ########
#to take top 5 to n records [DataFrame and Series]
df.head()
df.head(2)

a.head()
a.head(2)

#to take last n to 5 records [DataFrame and Series]
df.tail()
df.tail(2)

a.tail()
a.tail(3)

# Normal Select a columns information
df['B']

# To get a columns as Nx1 Matrix
aa=df[['B']]

# To get a range of rows
df[1:3]
