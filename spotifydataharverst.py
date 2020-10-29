# You are about to this endpoint: https://developer.spotify.com/console/get-current-user-top-artists-and-tracks
# IMPORTANT!!! Get a new OAuth Token: click token and select user-read-recently-played at the bottom right
# Run the script, click apidata.csv in your Repl.it
# Select the contents wihtin that file and copy it to an empty plain text text editor file. Save as apidata.csv
# Upload it to Toledo

import json
import requests
import pandas as pd
import uuid

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQC7xQbsOfHTL4u1Uxr6jvXa7N66Q6VuLgdUilUdTPMgF8czT1zFV2SLMJk5BvWoMHWST4CqRazL14Ek8DuwMMH92gCljWlfRvPP-q1f9xLVJJXHPJDuieQpJ0Hu0CrNkG89L02XIUcP3Z9XIHvqBBCvtF9DKaCBVc2mWlkLtB8QSlJsHfkKSmDBV7Pk_p-F1vthBqjDipMYSVTpd_c5d1ulNrbEjgUC4JXUfE7dAYANiDGqssvP4rgy14BvrhMkdTPUWwiG5nX5nRTfQg',
}

params = (
    ('time_range', 'short_term'),
    ('offset', '5'),
)

response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=headers, params=params)

json_data = json.loads(response.text) # convert json response to text/dict

data = []

id = uuid.uuid4()

for item in json_data['items']:
	name = item['name']
	genres = ', '.join(item['genres'])

	data.append({'id':id,'name':name,'genres':genres})

print(data)

data = pd.DataFrame(data)
data.to_csv('apidata.csv',sep=';',index=False)
