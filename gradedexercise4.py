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
			'Authorization': 'Bearer BQC4vJ4ibmBqDy0zZezzMaH4AVHBATK5P3BN31RE-tmI-pfVA7cmZMDGxT86i5LYS_ojk7GR75hMD2wxiurVkQH64ZfcI5Hx2lnxbBYYSMnTtwplscwf0On30GBDCxVaq6wMZF7nQ9DkV-xjtuXaHW5XKLZHSUbZ9rWQnNZlUTUVXOuZNl47kZl8BPULJiHd9teYi1meTE_zKTfDFnrdhGB1nANVeeY8gQiKO9HvimYgg3reXPdBhZxTpfbGw4qDrXjtH2_khOBBAEUtjQ',
	} # You will need to change the authorization key into an active one, this one will be expired - Get it - when you are logged in to Spotify - from https://developer.spotify.com/console/get-search-item/?q=tania%20bowra&type=artist&market=&limit=&offset= (scroll down and click get Token (DO NOT USE SAFARI AS YOUR BROWSER)

	params = (
					('q', item['Artist']), # Per iteration, the value of q = the read artist
					('type', 'artist'),
			)

	response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params) # request the response
	# The endpoint base url is supplemented by the arguments in the variables headers and params

	json_data = json.loads(response.text) # convert json response to text/dict
	imgurl = json_data['artists']['items'][0]['images'][0]['url']
	print(imgurl)
	
	imgfile = open(item['Artist']+'.jpg','wb') # Create a new, empty picture file
	imgfile.write(urlopen(imgurl).read()) # Write picture information into empty file
	imgfile.close() # Close file
	print('Picture downloaded...')
