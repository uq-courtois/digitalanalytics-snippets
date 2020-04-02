print(df.info() # Give overview of data types (see last column)

print(df['year'].unique()) # Print all unique values
df['year'] = df['year'].str[-5:-1] # Retaining a specific range
print(df['year'].unique()) # Print all unique values

print(df['duration'].unique()) # Print all unique values
df['duration'] = df['duration'].str.replace(' min','') # Replacing specific values
print(df['duration'].unique()) # Print all unique values

print(df['votes'].unique()) # Print all unique values
df['votes'] = df['votes'].str.replace(',','') # Replacing specific values
print(df['votes'].unique()) # Print all unique values

df.to_csv(r'imdb_data_recoded.csv', sep = ';') # Save processed version of data file
df = pd.read_csv('imdb_data_recoded.csv', sep = ';') # Import new version of data file

print(df.info() # Give overview of data types (see last column)
