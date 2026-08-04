import pandas as pd
df = pd.read_csv('pokemon_data.csv')


print(  df.loc[df['Name'].str.contains('Mega')]  )     # shows that contain 'Mega'

print(  df.loc[~df['Name'].str.contains('Mega')] )      # shows that doenot contain 'Mega'
