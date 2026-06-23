import pandas as pd
import numpy as np

dict1 = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
frame=pd.DataFrame(dict1)
frame2 = pd.DataFrame(dict1, index=['a', 'b', 'c'], columns=['Name', 'City','debt'])

print(frame)
print(frame.head(2))
print(frame.tail(2))
print(frame2)
print(frame2.columns)
print(frame.index)
print(frame['Name'])
print(frame['City'])
print(frame['Age'])
print(frame.Age)
print(frame2.loc['a'])
print(frame2.iloc[1])
frame2['debt'] = [1000, 2000, 3000]
print(frame2)
frame2['debt']=np.arange(3.0, 6.0, 1.0)
print(frame2)
val=pd.Series([1, 2, 3], index=['e', 'f', 'g'])
frame2['debt']=val
print(frame2)
frame2['debt']=frame['Age']==30
print(frame2)
frame2['balance']=frame2['Name']=='Bob'
print(frame2)