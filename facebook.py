### DO NOT CHANGE
from facebook_scraper import get_posts
from datetime import datetime, timedelta
import pandas as pd
import openpyxl
###

### PARAMETERS YOU SHOULD SET:
# Add @mentions or #hashtags as queries
pagenames = ['abc','theguardianaustralia']

### DO NOT CHANGE ANYTHING BEYOND THIS LINE
fbdata = []
ignorepin = 0
 
for pagename in pagenames:
	for post in get_posts(pagename, pages=5):
		print(pagename)
		print(post['text'])
		print(post['time'])

		fbdata.append(
			{'page':pagename,
			'text':post['text'],
			'time':post['time']}
		)

print('Successfully harvested',len(fbdata),'Facebook posts')

df = pd.DataFrame(fbdata) 
df.to_excel('fbdata.xlsx')
df.to_csv('fbdata.csv',sep=';',index=None)
###
