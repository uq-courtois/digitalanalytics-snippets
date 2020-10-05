### Revise EXERCISE 3 (Module 2)
 
# Read the data from searchresults.csv (http://www.cedriccourtois.be/files/searchresults.csv)
# Print the unique domain names extracted from all results (url variable in the data file)
# Count the number of times ‘hln.be’ is in the results
# Make a new csv file with only the top 3 ranked results (name it searchresults_top3.csv)

# Import pandas
import pandas as pd

data = pd.read_csv('searchresult.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

urllist = [] # empty list to store all domain names we're about the extract from the page urls

# Iterate through the imported data
for item in data:
	urllist.append(item['URL'].split('/')[0])
# We get the value for the URL key in each iteration
# We split on the /, which returns a list with the url in bits and pieces
# The first bit (or element in that list), is the domain name
# We append that domain name to urllist

print(set(urllist)) # We print urllist as a set so we're sure that there are no duplicates, only uniques
print(urllist.count('www.hln.be')) # We count the amount of times www.hln.be is in the list (this is on the list, not a set version of it)

topthree = [] # empty list that will be our list of dictionaries with top three results we want to export in a file

for item in data:
	if item['Rank'] < 4: # Conditional to make sure we only add information of top three results
		print(item['URL'],item['Rank']) # Just printing the top three resuls' URL and Rank
		topthree.append({'URL':item['URL'],'Rank':item['Rank']}) # topthree list - empty before loop - is populated with top 3 results
# Note that we are adding a dictionary to the list per iteration, containing the iteration value of URL and Rank

### Exercise 1

#1 Read data from the file articletitles.csv with two variables: Title and URL (Download the file from http://www.cedriccourtois.be/files/articletitles.csv) and convert into a list of dictionaries
#2 Add a new key called TitleLower to your list of dictionaries. The value should be the value of Title converted into lowercase (use the .lower() method, e.g., to convert a variable 'Var' into lowercase, you use Var = Var.lower()
#3 Indicate whether the lowercase conversion of the title contains 'covid' or 'corona' (possible values are 'Yes' or 'No' - This will be another added key, called CoronaMention)
#4 Write a new file articletitles_processed.csv with four variables: Title, TitleLower,  URL, CoronaMention

### Exercise 2

#1 Read the data from the file diameters.csv (http://www.cedriccourtois.be/files/diameters.csv)
#2 Calculate the circumference of a circle based on the given diameter values (formula: pi * diameter. Remember: pi = 3.14) and add that value in a key 'circumference’
#3 Print the observationids of all circles with a circumference larger than 10
#4 Write a new file with the observationids, the diameters, and the circumference as variables. Name the file circles.csv
