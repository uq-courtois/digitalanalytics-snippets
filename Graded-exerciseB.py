### Read date from the file articletitles.csv with two variables: Title and URL (Download the file from http://www.cedriccourtois.be/files/articletitles.csv) and convert into a list of dictionaries

# Code adapted from Module 2: Read data

import pandas as pd

data = pd.read_csv('http://www.cedriccourtois.be/files/articletitles.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

for item in data: # Not necessary, but temporarily helpful to check whether everthing worked, and to get to know the data
	print(item)

### Add a new key called TitleLower to your list of dictionaries. The value should be the value of Title converted into lowercase (use the .lower() method, e.g., to convert a variable 'Var' into lowercase, you use Var = Var.lower()

# Code adapted from Module 1: Exercise 11 on for loops - We're adding a key there as well, based on existing key-value data

for item in data:
    item['TitleLower'] = item['Title'].lower()

    ### Indicate whether the lowercase conversion of the title contains 'covid' or 'corona' (possible values are 'Yes' or 'No' - This will be another added key, called CoronaMention)

    # Code adapted from Module 1: Conditionals + See Module 1: exercise 3 for the 'string' in objectx formula

    if 'covid' in item['TitleLower'] or 'corona' in item['TitleLower']: # NOT 'covid' or 'corona' in ... !!!
        item['CoronaMention'] = 'Yes'
    else:
        item['CoronaMention'] = 'No'

### Write a new file articletitles_processed.csv with four variables: Title, TitleLower,  URL, CoronaMention

# Code adapted from Module 2: Write data

data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('articletitles_processed.csv',sep=';',index=False) # Writing dataframe into CSV file

# Tip: Always check whether your output data make sense: open the file, eyeball it...
