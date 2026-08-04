
import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.loc[df['Type 1'] == 'Normal'])          ## Single Condition # Condition that at row,column "Type 1" where is "Fire" print it