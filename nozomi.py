# An example of an item in the original list, a url refering to a specific webpage

url = 'https://www.abc.net.au/news/2020-03-11/bear-market-share-stocks-investing-superannuation-coronavirus/12046630'

# We want to get to the domain name 'www.abc.net.au'
# To do that, we need to split that string value on each /

decomposed = url.split('/')
print(decomposed)

# Composed is a list with the following values: ['https:', '', 'www.abc.net.au', 'news', '2020-03-11', 'bear-market-share-stocks-investing-superannuation-coronavirus', '12046630']
# We need to get the third element (1,2,3), which has an index 2 (0,1,2)

print(decomposed[2])

# I'm not sure about your second question. After converting to a set and turning back into a list, it should have dropped from 5 to 2 elements.
# In the list domainnames that you have after the loop, there are duplicates. There's 2 sets of either 3 or 2 of the same domainnames. To keep only the unique domainnames, we convert to a set (which drops te duplicates, and then get back to a list from that set)

domainnames = [
'www.news.com.au',
'www.news.com.au',
'www.news.com.au',
'www.abc.net.au',
'www.abc.net.au',
]

print(domainnames) # List contains duplicats, i.e., exact copies of the same value. That the original urls had specific page information is not relevant anymore, because now we are dealing with the domain names)
print(list(set(domainnames))) # List contains no duplicates
