import pandas as pd

df = pd.read_csv('imdb_data_recoded.csv', delimiter = ';')

print(df['countries'].str.split(',').explode().unique()) # Print all the unique elements in the variable countries

countrydata = pd.read_csv('countries-continents.csv', sep=',') # Read external country data - a list with actual countries
countrydata = countrydata.T.to_dict().values() # Transform into a list of dictionaries

#####
##### Following function is activated in the lambda function below

def location_categorisation(x):
	
	countries = [] # Empty list that will store the actual countries found in each value of x (i.e., value of variable countries that is processed at the time)

	for item in countrydata:
		try:
			if item['Country'] in x:
				countries.append(item['Country']) # Adding a country to the list when it is found in x
		except:
			pass

	print('Found',len(countries),'countries in',x,'-',countries) # Summarizing how many countries were found in a value of x

  ### The conditionals that channel the actual categorisation:

	if 'USA' in countries and len(countries) == 1:
		return 'USA'
	if 'USA' in countries and len(countries) > 1:
		return 'Coproduction'
	if 'USA' not in countries and len(countries) >= 1:
		return 'Non-USA'
    
######
######

df['productionlocation'] = df['countries'].apply(lambda x: location_categorisation(x)) # For every value in the variable countries a labmda function applies the function location_categorisation

print(df[['countries','productionlocation']].head(40)) # Shows the final result: a new variable (and old variable shown as comparison)
