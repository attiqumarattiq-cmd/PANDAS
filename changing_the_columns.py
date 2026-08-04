import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:11]]                         # According to this sequence the column prints
print(df)

# [cols[-1]], it represents the last column