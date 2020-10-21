### EXERCISE A

### Credentials: https://developers.google.com/maps/documentation/geocoding/get-api-key#get-the-api-key
 
import json
from urllib.request import urlopen
 
baseurl = "https://maps.googleapis.com/maps/api/geocode/json?" # Endpoint URL
query = "address=" + "Social Sciences KU Leuven" # Build query for address argument
query = query.replace(' ','+') # Replace spaces in query with +
apikey = "&key=AIzaSyBgNKboBAT2qCTUTvC0CvJbYLhg5yIVtEY" # API key - you will need to get your own to try this example
# I deactivated the API key in this example for safety reasons
 
compiledurl = baseurl + query + apikey # Combining all the url components into a single url
 
json_object = urlopen(compiledurl) # Send request + get response
locationdata = json.load(json_object) # Convert JSON result
 

print(locationdata['results'][0]['geometry']['location']['lat'])
print(locationdata['results'][0]['geometry']['location']['lng'])

###

# -*- coding: utf-8 -*-

import json
import requests
import pandas as pd
from urllib.request import Request, urlopen

data = pd.read_csv('http://www.cedriccourtois.be/files/artists.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

dataset = [] # Empty list to temporarily save the new data, and at the end write it into a new CSV

# Iterate through the imported data
for item in data:
	print('Searching for',item['Artist'])

	headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'Authorization': 'Bearer BQCWr1OATUJqVf7wWTKVmRVfqw-Ji3nodnlWGgVaso0rhH6e7IJOu3jhBPnYtBHDrImVyeGAEZsMq9WleKt0FNl9WAdQDwZ4UKNdhhIbJz1Pxib_V5zDReXFpqrRAtLSs2B5SPYpQA5TDy5ALcBm01BXBqAGDVZRU18o_nIsOC4eNdzLALfrCBEE7KvLhd9ttYy28wfHPHsH03f7KuF4VUQytcaQZlIOVDKQePxq8uUQ6NliEILuSPUleJlqbw1_TByYEcrZ95O0zAs1HQ',
	} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

	params = (
					('q', item['Artist']), # Per iteration, the value of q = the read artist
					('type', 'artist'),
			)

	response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
	# The endpoint base url is supplemented by the arguments in the variables headers and params

	json_data = json.loads(response.text) # convert json response to text/dict
	
	imgfile = open(item['Artist']+'.jpg','wb') # Create a new, empty picture file
	imgfile.write(urlopen(json_data['artists']['items'][0]['images'][0]['url']).read()) # Write picture information into empty file
	imgfile.close() # Close file
