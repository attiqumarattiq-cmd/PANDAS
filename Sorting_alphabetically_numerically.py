import pandas as pd 
df = pd.read_csv('pokemon_data.csv')


## Sorting the columns, Write the data of "Name"  Column in alphabetical order 
df = df.sort_values(['Name'] , ascending = True )    # (A-Z)
df = df.sort_values(['Name'] , ascending = False )   # (Z-A)


## Sorting of the column that contains number is ascending and descending order
df = df.sort_values(['HP'], ascending = True)      # In ascending order
df = df.sort_values(['HP'], ascending = False)      # In descending order
















