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
