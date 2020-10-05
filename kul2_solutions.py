### Exercise 1

#1 Read data from the file articletitles.csv with two variables: Title and URL (Download the file from http://www.cedriccourtois.be/files/articletitles.csv) and convert into a list of dictionaries
#2 Add a new key called TitleLower to your list of dictionaries. The value should be the value of Title converted into lowercase (use the .lower() method, e.g., to convert a variable 'Var' into lowercase, you use Var = Var.lower()
#3 Indicate whether the lowercase conversion of the title contains 'covid' or 'corona' (possible values are 'Yes' or 'No' - This will be another added key, called CoronaMention)
#4 Write a new file articletitles_processed.csv with four variables: Title, TitleLower,  URL, CoronaMention

import pandas as pd
 
data = pd.read_csv('http://www.cedriccourtois.be/files/articletitles.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries
 
# Iterate through the imported data
for item in data:
	item['TitleLower'] = item['Title'].lower()
	if 'covid' in item['TitleLower'] or 'corona' in item['TitleLower']:
		item['CoronaMention'] = 'Yes'
		print(item['Title']) # Not needed, but a nice check
	else:
		item['CoronaMention'] = 'No'

newdata = pd.DataFrame(data) # Converting list of dictionaries into dataframe
newdata.to_csv('articletitles_processed.csv',sep=';',index=False) # Writing dataframe into CSV file

### Exercise 2

#1 Read the data from the file diameters.csv (http://www.cedriccourtois.be/files/diameters.csv)
#2 Calculate the circumference of a circle based on the given diameter values (formula: pi * diameter. Remember: pi = 3.14) and add that value in a key 'circumference’
#3 Print the observationids of all circles with a circumference larger than 10
#4 Write a new file with the observationids, the diameters, and the circumference as variables. Name the file circles.csv

import pandas as pd
 
data = pd.read_csv('http://www.cedriccourtois.be/files/diameters.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

for item in data:
	item['circumference'] = 3.14 * item['diameter']
	if item['circumference'] > 10:
		print(item['observationid'])

newdata = pd.DataFrame(data) # Converting list of dictionaries into dataframe
newdata.to_csv('circles.csv',sep=';',index=False) # Writing dataframe into CSV file
