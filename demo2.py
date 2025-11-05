import numpy as np
import pandas as pd
id=['a','b','c','d','e','f','g','h']
d1=pd.DataFrame(np.arange(32).reshape(8,4),index=id,columns=['A','B','C','D'])
print(d1)