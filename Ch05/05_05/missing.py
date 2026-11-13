# %%
import pandas as pd


df = pd.read_csv('cart.csv', parse_dates=['date'])
df

# %% 
# fill missing values in the 'amount' column with 1
df['amount'].fillna(1, inplace=True)
df

# %%
most_common = df['name'].mode()[0]
df['name'].fillna(most_common, inplace=True)
df

# %%
df['date'].fillna(method='ffill', inplace=True)
df

# %%
import numpy as np
# calculate the mean price for each item to fill missing values
prices = df.groupby('name')['price'].transform(np.mean)
prices

# %%
df['price'].fillna(prices, inplace=True)
df