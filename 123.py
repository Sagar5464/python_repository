import numpy as np
import pandas as pd
df = pd.DataFrame([[1, np.nan, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6]])
print(df)
print(df.fillna(method='bfill', axis=0))
print(df.fillna(method='bfill', axis=1))


import numpy as np
import pandas as pd
df = pd.DataFrame([[1, np.nan, 2,np.nan],
                   [2, 3, 5,np.nan],
                   [np.nan, 4, 6,np.nan],
                    [np.nan, 8, np.nan,np.nan],
                    [np.nan, np.nan, np.nan,np.nan]])
print(df)
print(df.fillna(999)).           m. 



     