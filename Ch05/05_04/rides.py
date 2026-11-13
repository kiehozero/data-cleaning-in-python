# %%

import pandas as pd

df = pd.read_csv('rides.csv')
df

# %%
# you can pass criteria to the eval function to create a mask for bad 
# rows, and you can string these together using and or or operators
mask = df.eval('name.isnull() | distance <= 0')
mask

# %%
df = df[~mask]
df
