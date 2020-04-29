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
maindiv = soup.find('div',class_="sf_colsIn col-md-10")

#print(maindiv)

dataset = []

for item in maindiv('a'):
	title = item.find('p').getText()
	url = item['href']
	print(title)
	print(url)
	print()

	dataset.append({'title':title,'url':url})

dataset = pd.DataFrame(dataset) # Converting list of dictionaries into dataframe
dataset.to_csv('who-news.csv',sep=';',index=False) # Writing dataframe into CSV file
