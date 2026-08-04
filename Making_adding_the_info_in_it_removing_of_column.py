
import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

#================================================================================================================================================
# --------------------------- FIRST METHOD (NOT EFFICIENT) ----------------------
## Making a new column in data, and assigning value by other column of there addition
# Note that "Total" column doesnot exist before
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] + df['Generation'] + df['Legendary']



# -------------------------- SECOND METHOD (BEST AND HAS MORE PROPERTIES) ----------------------
## Making new column named as "Total" , it sum up from 4th  to 11 value adding horizontally it gives value to "Total" to that row
df['Total'] = df.iloc[:, 4: 11].sum( axis = 1)    # axis=1 shows means adding horizontally, axis=0 shows means adding vertically 

df['Total'] = df.iloc[ 2:4, 4:11].sum( axis = 1)  # Only adding the number from row 2 to row 4
#=====================================================================================================================================================

# ---------------- Removing and deleting -------------------
df = df.drop(columns = 'Total')                 ## IT remove or delete the column "Total"

df = df.drop(columns = 'Legendary')            ## It removes the column "Legendary"

df = df.drop(index = [2,3,4])                 ## Remove the rows by indexing the numbers


#=========================================================================================================================================



