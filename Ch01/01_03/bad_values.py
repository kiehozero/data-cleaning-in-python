# %%
import pandas as pd

# %%
df = pd.read_csv('metrics.csv', parse_dates=['time'])
df.sample(10)

# %%
df.groupby('name').describe()

# %%
# Count the occurrences of each unique value in the 'name' column
df['name'].value_counts()

# %%
# Pivot the data to visualize each metric over time
pd.pivot(df, index='time', columns='name').plot(subplots=True)

# %%
# Identify bad CPU values based on a threshold
df.query('name == "cpu" & (value < 0 | value > 100)')

# %% 
mem = df[df['name'] == 'mem']['value']
z_score = (mem - mem.mean())/mem.std()
bad_mem = mem[z_score.abs() > 2]
# bad_mem
df.loc[bad_mem.index]
