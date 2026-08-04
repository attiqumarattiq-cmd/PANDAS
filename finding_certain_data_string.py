import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

print(df.loc[df['Name'].str.contains('Mega')])

#print(df.loc[df['Type 1'].str.contains('Fire|Grass')])