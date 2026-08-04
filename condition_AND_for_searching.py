
import pandas as pd
df  = pd.read_csv('pokemon_data.csv')

print(df.loc[ (df['Type 1'] == 'Normal')   &  (df['Type 2'] == 'Flying')  ])

## It prints that row in which both condition matches 
                      # means in that column where "Type 1" is "Normal" and "Type 2" is "Flying"
