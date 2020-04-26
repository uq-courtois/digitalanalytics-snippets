#EXERCISE 1

	#1.	Read the data from the file articlestitles.csv (http://www.cedriccourtois.be/files/articletitles.csv)
	#2.	Add a new key called TitleLower to your list of dictionaries. The value should be the value of Title converted into lowercase (use the .lower() method, e.g., to convert a variable 'Var' into lowercase, you use Var = Var.lower()
	#3.	Programatically count the number of article titles (use TitleLower) that contain 'corona' or 'covid'
	#•	Tip: one way to count is by setting a count variable to 0 before starting a loop and update it +1 for every relevant iteration - we used this approach once before in a module exercise!)
	#4.	Print the number (i.e., one, final number!) of articles at the end of the program (do not print the titles)

import pandas as pd

data = pd.read_csv('http://www.cedriccourtois.be/files/articletitles.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

count = 0

for item in data:
	item['TitleLower'] = item['Title'].lower()
	if 'covid' in item['TitleLower'] or 'corona' in item['TitleLower']:
		count += 1

print(count)

#EXERCISE 2
	#1.	Read the data from the file diameters.csv (http://www.cedriccourtois.be/files/diameters.csv)
	#2.	Calculate the circumference of a circle based on the given diameter values (formula: pi * diameter. Remember: pi = 3.14) and add that value in a key 'circumference'
	#3.	Print the observationids of all circles with a circumference larger than 10
	#4.	Write a new file with the observationids, the diameters, and the circumference as variables. Name the file circles.csv

import pandas as pd

data = pd.read_csv('http://www.cedriccourtois.be/files/diameters.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionarie

for item in data:
	item['circumference'] = item['diameter'] * 3.14
	if item['circumference'] > 10:
		print(item['observationid'])

data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('circles.csv',sep=';',index=False) # Writing dataframe into CSV file
