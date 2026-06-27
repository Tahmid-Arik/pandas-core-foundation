import pandas as pd
import numpy as np
s1=pd.Series([4.8,3.3,2.1,7.8],index=["z","x","w","y"])
s2=s1.reindex(["x","y","z","w","v"])
print(s1)
print(s2)
s3=pd.DataFrame(np.arange(16,32).reshape((4,4)),index=[1,2,3,4],columns=["A","B","C","D"])
print(s3)
s4=s3.reindex(index=[5,1,3,8])
print(s4)
l=['B','Y','D','C']
s5=s3.reindex(l,axis=1)
print(s5)
s6=s3.reindex(index=[5,1,3,8],fill_value=6)
print(s6)
