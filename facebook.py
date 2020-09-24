### DO NOT CHANGE
from facebook_scraper import get_posts
from datetime import datetime, timedelta
import pandas as pd
import openpyxl
###

### PARAMETERS YOU SHOULD SET:
# Add @mentions or #hashtags as queries
pagenames = ['abc']

### DO NOT CHANGE ANYTHING BEYOND THIS LINE
fbdata = []
ignorepin = 0
 
for pagename in pagenames:
	for post in get_posts(pagename, pages=99):
		post['query'] = pagename
		print(pagename,'- Harvested post',post['text'])
		print('Posted on',post['time'])
		fbdata.append(post)

print('Successfully harvested',len(fbdata),'Facebook posts')

df = pd.DataFrame(fbdata) 
df.to_excel('fbdata.xlsx')
###
