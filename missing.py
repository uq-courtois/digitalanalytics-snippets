print(df.isnull().sum()) # Get summary of variables' missing data count

isolatemissing = pd.isnull(df['metascore'])
# Creates a Boolean pool of missing rows to isolate the missing values for variable 'metascore'

print(df[isolatemissing]) # Print rows with missing data

df.dropna() # Drop rows with at least one missing entry
