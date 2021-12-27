import pandas as pd
import numpy as np
 
# Step 1: Read the data
df = pd.read_csv('df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/consolidated_omdb.csv', delimiter = ',')
 
# Step 2: Get an overview of the variables
print(df.info())
 
# Step 3: Get an overview of the values
print(df['Error'].unique())
print(len(df['Error'].unique()))
subset = df[df['Error'] == 'Incorrect IMDb ID.']
print(subset['imdburl'])

# Step 4: Check for duplicates
print('\n# Exact duplicates:',df.duplicated().sum()) 
print('\n# Rows with duplicates:\n',df[df.duplicated()])

# Step 5: Check for missing values
print('\n # Missing data:\n',df.isnull().sum())

print('\n# Shape before removing missings:\n',df.shape)
df = df.dropna(subset=['Title','imdbRating','Country','Language']) # Get rid of observations in year with missing values
print('\n# Shape after removing missings:\n',df.shape)

# Step 6: Convert strings into numerics
print(df['Year'].head(10)) # print 10 first observations
df['Year'] = df['Year'].str[:4].astype(int)
print(df['Year'].head(10)) # print 10 first observations

# Step 6: Create categorisations

### Divide between productions that contain English or do not

print(df['Language'].head(25))

def language_categorisation(Language):
	if 'English' in Language:
		english = 'yes'
	else:
		english = 'no'
	return english
	
df['english'] = df['Language'].apply(lambda x: language_categorisation(x))
print(df[['Language','english']])

### Divide location of production studio in only USA, collaborations between USA and others, and only others

print(df['Country'].head(25))

def location_catergorisation(Country):
	productionlocation = ''

	if type(Country) == str:
		Country = Country.split(', ')
		if 'United States' in Country and len(Country) == 1:
			productionlocation = 'USA only'
		if 'United States' not in Country and len(Country) >= 1:
			productionlocation = 'Non-USA'
		if 'United States' in Country and len(Country) > 1:
			productionlocation = 'Coproduction'

		return productionlocation

df['productionlocation'] = df['Country'].apply(lambda x: location_catergorisation(x))
print(df[['Country','productionlocation']])

# Step 7: Get final overview
print(df.info())

# Step 8: Write data into clean file without row numbers
df.to_csv('imdb_data_clean.csv',index=False)
