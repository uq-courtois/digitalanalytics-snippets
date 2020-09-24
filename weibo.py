### DO NOT CHANGE
from weibo_scraper import  get_weibo_tweets_by_name
from datetime import datetime, timedelta
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup

###

### PARAMETERS YOU SHOULD SET:
# Accounts you want to scrape

searchqueries = ['嘻红豆']

### DO NOT CHANGE ANYTHING BEYOND THIS LINE
twitterdata = []
 
for searchquery in searchqueries:
	print(searchquery)
	print('---')
	for tweet in get_weibo_tweets_by_name(name=searchquery, pages=None):
		soup = BeautifulSoup(tweet['mblog']['text'], 'html.parser')
		text = soup.getText()
		id = tweet['itemid']
		created = tweet['mblog']['created_at']

		print(text,'posted on',created)
		
		twitterdata.append(
			{'id':id,
			'text':text,
			'created':created,
			'author':searchquery}
		)

print('Successfully harvested',len(twitterdata),'posts')

df = pd.DataFrame(twitterdata) 
df.to_csv('weibodata.csv',sep=';',index=None)
df.to_excel('weibodata.xlsx')
###
