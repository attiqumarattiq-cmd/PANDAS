import pandas as pd 
df = pd.read_csv('pokemon_data.csv')

# print(df.head(3))             ## PRINT THE FIRST THREE ROWS

# print(df.tail(3))             ## PRINT FROM LAST THREE ROWS

#for index, row in df.iterrows():         ## ACESSING THE DATA IN EACH INVIDUAL HORIZONTAL LINE ONE AT A TIME
    #print(index, row['Name'])

# print(df.iloc[0:4])                    ## READ EACH ROW

# print(df.iloc[18,5])                      ## READ SPECIFIC LOACATION IN ROWS AND COLUMNS

# for index, row in df.iterrows():
    # print(index, row['Type 1'])               ## ACCESSING THE DATA IN EACH Individual horizontal line one at a time

# print(df.describe())                          ## It calculates the mean, max, min etc of the data ### IMPORTANT



# print(cols = df.columns.values)                  ## Print the name of all columns

# df = df[['Attack', 'HP', 'Defense']]              ## Print the data of the specified column
# print(df.head(5))





 