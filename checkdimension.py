import pandas as pd

df = pd.read_csv('imdb_data.csv', delimiter = ';') # Import data

print(df.info()) # Print information on dataframe df

print(df) # Print overview of df values

pd.set_option('display.max_columns',10) # Forcing to show all 10 colums
print(df) # Print overview of df values

print(df['title']) # Overview one variable
print(df[['title','year']]) # Overview two or more variables

print(df['title'].head(30)) # Get the 30 first values of the title variable

# Subset (narrow down) df to a particular value for a variable and storing as a new df called subset
subset = df[df['title'] == 'Lady and the Tramp']
print(subset[['title','year']]) # Print values for variables title and year in the dataframe called subset

# or shorter...
print(df[df['title'] == 'Lady and the Tramp'][['title','year']])
