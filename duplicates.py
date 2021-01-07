print(df[df['title'] == 'Lady and the Tramp'][['title','year']]) # lady and the Tramp before

### Get rid of exact duplicates 

print(df.duplicated().sum()) # Number of exact duplicates
print(df[df.duplicated()]) # Showing rows with duplicates
df = df.drop_duplicates() # Drop exact duplicates

### Get rid of duplicates for a subset of variables
### In this case records that have the same movie title, year of production, and duration

print(df.duplicated(subset=['title','year','duration']).sum()) # Number of duplicates with same title, year, duration
df = df.drop_duplicates(subset=['title','year','duration']) # Drop these duplicates

print(df[df['title'] == 'Lady and the Tramp'][['title','year']]) # lady and the Tramp after
