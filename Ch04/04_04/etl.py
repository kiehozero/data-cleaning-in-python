# %%
import pandas as pd

df = pd.read_csv('ships.csv')
df

# %%
import sqlite3

# this query is deliberately designed to fail because of a non-null
# constraint on the lat and lng columns, in the 04_06 files you'll
# see how it is fixed
schema = '''
CREATE TABLE ships (
    name TEXT,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL
);
'''

db_file = 'ships.db'
conn = sqlite3.connect(db_file)
conn.executescript(schema)

try:
    with conn as cur:
        cur.execute('BEGIN')
        df.to_sql('ships', conn, if_exists='append', index=False)
finally:
    conn.close()
