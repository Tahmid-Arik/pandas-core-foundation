import pandas as pd
import numpy as np
onj=pd.Series([1,-2,3,-4,5], index=["one","two","three","four","five"])
print(np.exp(onj))
m="three" in onj
print(m)
print(onj.to_dict())

dict1={"one":1,"two":-2,"three":3,"four":-4,"five":5}
print(dict1)
onj1=pd.Series(dict1)
print(onj1)

ind=["one","two","three","four","five","six"]
onj2=pd.Series(dict1,index=ind)
print(onj2)
print(onj2.isna())
print(onj2.notna())