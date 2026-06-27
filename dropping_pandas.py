import pandas as pd
import numpy as np
s1=pd.Series(np.arange(3.0),index=['a','b','c'])
new_s1=s1.drop(['a','c'])
print(s1)
print(new_s1)
s2=pd.DataFrame(np.arange(16,32).reshape(4,4),index=[1,2,3,4],columns=['a','b','c','d'])
print(s2)
print(s2.drop(columns=['c']))
print(s2.drop(index=[2,3]))