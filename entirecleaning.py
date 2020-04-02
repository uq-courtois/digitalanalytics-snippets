import pandas as pd
 
df = pd.read_csv('imdb_data.csv', delimiter = ';') # Import data
 
df = df.drop_duplicates(subset=['title','year','duration']) # Drop duplicates

df['year'] = df['year'].str[-5:-1] # Fix year variable
df['duration'] = df['duration'].str.replace(' min','') # Fix duration variable
df['votes'] = df['votes'].str.replace(',','') # Fix votes variable

df['sfxgenre'] = df['genres'].apply(lambda x: 'higher sfx' if 'Action' in x or 'Fantasy' in x or 'Sci-Fi' in x or 'Adventure' in x or 'Animation' in x else 'lower sfx') # Categorisation of genres

countrydata = pd.read_csv('countries-continents.csv', sep=',') # Read external country data
countrydata = countrydata.T.to_dict().values() # Transform into a list of dictionaries
  
def location_categorisation(x):
	
	countries = [] # Empty list that will store the actual countries found in each value of x
 
	for item in countrydata:
		try:
			if item['Country'] in x:
				countries.append(item['Country']) # Adding a country to the list when it is found in x
		except:
			pass
 
  ### The conditionals that channel the actual categorisation:
	if 'USA' in countries and len(countries) == 1:
		return 'USA'
	if 'USA' in countries and len(countries) > 1:
		return 'Coproduction'
	if 'USA' not in countries and len(countries) >= 1:
		return 'Non-USA'
 
df['productionlocation'] = df['countries'].apply(lambda x: location_categorisation(x)) # For every value in the variable countries a labmda function applies the function location_categorisation

df['agefilm'] = 2020 - df['year'].astype(float) # Calculate age of movie

df.to_csv(r'imdb_data_clean.csv', sep = ';') # Save processed version of data file
df = pd.read_csv('imdb_data_clean.csv', sep = ';') # Import new version of data file
 
print(df.info()) # Give overview of data types (see last column)
pd.set_option('display.max_columns',10) # Forcing to show all 10 colums
print(df) # Give overview of values
