import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(1,21).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['col1','col2','col3','col4'])
print(data)
print(data.iloc[:,:][data.col4>11])

print(data.iloc[-1])
print(data.loc['row4'])

m=data.loc[data.col4==12]["col4"]=6
print(m)
data.loc[data.col4==12,"col4"]=7
print(data)

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
s2=pd.Series([5,6,7,8,9,10],index=['a','b','c','d','e','f'])
print(s1+s2)

df1=pd.DataFrame(np.arange(1,13).reshape(3,4),index=['row1','row2','row3'],columns=['col1','col2','col3','col4'])
print(df1)
df2=pd.DataFrame(np.arange(1,13).reshape(4,3),index=['row1','row2','row3','row4'],columns=['col1','col2','col3'])
print(df2)
df2.loc["row1","col2"]=13
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=0))

n=df1.reindex(columns=df2.columns,fill_value=0)
print(n)