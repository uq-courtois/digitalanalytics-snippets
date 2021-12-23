import pandas as pd

# Step 1: Read the data
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/imdb_data.csv', delimiter = ',')

# Step 2: Get an overview of the variables
print(df.info())

# Step 3: Check for duplicates
print('\n# Exact duplicates:',df.duplicated().sum()) 
print('\n# Rows with duplicates:\n',df[df.duplicated()])
print('\n# Shape before removing duplicates:\n',df.shape)
df = df.drop_duplicates() # Get rid of duplicates
print('\n# Shape after removing duplicates:\n',df.shape)

# Step 4: Check for missing values
print('\n # Missing data:\n',df.isnull().sum())
isolatemissing = pd.isnull(df['year'])
print('\n Rows with missing data in year:\n',df[isolatemissing])
print('\n# Shape before removing missings:\n',df.shape)
df = df.dropna(subset=['year']) # Get rid of observations in year with missing values
print('\n# Shape after removing missings:\n',df.shape)

# Step 5: Convert strings into numerics
print(df['year'].head(25)) # print 25 first observations
df['year'] = df['year'].str[-5:-1].astype(int)
print(df['year'].head(25)) # print 25 first observations

# Step 6: Create categorisations

### Divide between genres prone to special effects and those less so

print(df['genres'].head(25))

def specialeffects(genres):
	if 'Action' in genres or 'Fantasy' in genres or 'Sci-Fi' in genres or 'Adventure' in genres or 'Animation' in genres:
		sfxgenre = 'higher sfx'
	else:
		sfxgenre = 'lower sfx'
	return sfxgenre
	
df['sfxgenre'] = df['genres'].apply(lambda x: specialeffects(x))
print(df[['genres','sfxgenre']])

### Divide location of production studio in only USA, collaborations between USA and others, and only others

print(df['countries'].head(25))

def location_catergorisation(countries):
	productionlocation = ''

	if type(countries) == str:
		countries = countries.split(',')
		if 'USA' in countries and len(countries) == 1:
			productionlocation = 'USA only'
		if 'USA' not in countries and len(countries) >= 1:
			productionlocation = 'Non-USA'
		if 'USA' in countries and len(countries) > 1:
			productionlocation = 'Coproduction'

		return productionlocation

df['productionlocation'] = df['countries'].apply(lambda x: location_catergorisation(x))
print(df[['productionlocation','countries']])

# Step 7: Get final overview
print(df.info())

# Step 8: Write data into clean file without row numbers
df.to_csv('imdb_data_clean.csv',index=False)
