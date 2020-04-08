from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# The URL we want to scrape
url = 'http://www.news.com.au' 

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
content = soup.find_all('div',class_ = 'group-content')

for item in content:
	for div in item.find_all('a'):
		print(div.getText().strip())
		print(div['href'])
