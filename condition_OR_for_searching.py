
import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

print(df.loc[ (df['Type 1'] == 'Normal')  |  (df['Type 2'] == 'Flying')  ])     

## Double Condition of OR # Condition that if "Type 1" has "Normal" written or "Type 2" has "Flying", print that column