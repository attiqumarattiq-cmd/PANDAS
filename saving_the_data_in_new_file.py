import pandas as pd
df = pd.read_csv('pokemon_data.csv')


df = df[['Attack', 'Defense', 'Type 1']]

df.to_csv('New1_file.csv', index = False)
df.to_csv('New2_file.csv')

#  In first statement, when code runs, it makes a new csv file named as 'New1_file.csv', in that file od csv, the datat shows but the index were not shown because index = 0
# in second statement, the index were present
