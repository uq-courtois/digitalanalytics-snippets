### DO NOT CHANGE
from twitter_scraper import get_tweets
from datetime import datetime, timedelta
import pandas as pd
import openpyxl
###

### PARAMETERS YOU SHOULD SET:
# Add @mentions or #hashtags as queries
searchqueries = ['@ladygaga','@billieeilish','@ritaora','@beyonce']
# Set a cut off date: how far back in time...
cutoffdate = datetime(2020, 1, 1, 00, 00, 00)
###

### DO NOT CHANGE ANYTHING BEYOND THIS LINE
twitterdata = []
ignorepin = 0
 
for searchquery in searchqueries:
	for tweet in get_tweets(searchquery):
		if cutoffdate < tweet['time']:
			tweet['query'] = searchquery
			print(searchquery,'- Harvested tweet posted on',tweet['time'])
			twitterdata.append(tweet)

		else:
			ignorepin += 1
			if ignorepin == 5:
				break

print('Successfully harvested',len(twitterdata),'tweets')

df = pd.DataFrame(twitterdata) 
df.to_excel('twitterdata.xlsx')
###
