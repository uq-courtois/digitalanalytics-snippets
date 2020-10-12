#####
##### EXERCISE 1

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd
 
# The URL we want to scrape
url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news' 
 
#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS
 
# Open URL (i.e., make request) + disguise agent
headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()
 
# To fetch html and store in variable 'html'
uClient= urlopen(req, context=context)
html = uClient.read() # html is stored in variable html
uClient.close()
 
#################################################
#################################################
 
### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')
maindiv = soup.find('div',class_='sf_colsIn col-md-9')

data = []

for item in maindiv.find_all('a'):
	
	title = item.find_all('p')[0].getText()

	try:
		dateinfo = item.find_all('p')[1].getText().split(' I')[0]
	except:

		try:
			dateinfo = item.find('span',class_='timestamp').getText()
		except:
			dateinfo = ''

	url = item['href']

	print(title)
	print(dateinfo)
	print(url)

	data.append({
		'title':title,
		'dateinfo':dateinfo,
		'url':url,
	})

data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('who-news.csv',sep=';',index=False) # Writing dataframe into CSV file

#####
##### EXERCISE 2

from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup
import pandas as pd

stop = 1001
counter = 0
baseurl = 'https://nieuws.kuleuven.be/en?b_start:int='
data = []

while counter < stop: 

	# The URL we want to scrape
	url = baseurl+str(counter)
	
	#################################################
	#################################################
	### COPY/PASTE THIS BLOCK AS IS
	
	# Open URL (i.e., make request) + disguise agent
	headers={'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	req = Request(url, headers=headers)
	context = ssl._create_unverified_context()
	
	# To fetch html and store in variable 'html'
	uClient= urlopen(req, context=context)
	html = uClient.read() # html is stored in variable html
	uClient.close()
	
	#################################################
	#################################################

	### Interpret the page source as html
	soup = BeautifulSoup(html, 'html.parser')

	for item in soup.find_all('div',class_='col-xs-12 col-md-6'):
		title = item.find('h2').find('a').getText().strip()
		url = item.find('h2').find('a')['href']
		print(title)
		print(url)
		print()

		data.append({
		'title':title,
		'url':url,
		})

	counter += 20

data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('kulnews.csv',sep=';',index=False) # Writing dataframe into CSV file
