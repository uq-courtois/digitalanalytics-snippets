from twitter_scraper import get_tweets # Import ready-made scraper module
# Additional documentation on the module: https://pypi.org/project/twitter-scraper/

searchquery = "@ladygaga" # Set a searchquery, which is a string value
# Could be an account => @... e.g., @ladygaga
# Could be a hashtage => #...

for tweet in get_tweets(searchquery): # Usually runs up to 500 iterations
	print(tweet) # Each iteration variable tweet is a dictionary with all relevant key-value pairs, for example: tweet['text'] is the key for the value of the actual tweeted text
	print()

# Adapt this script to run three consecutive queries instead of just one
# Adapt this script so the final results are written into an xlsx file
