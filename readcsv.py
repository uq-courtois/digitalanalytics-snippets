# READING

# Import pandas
import pandas as pd

data = pd.read_csv('newdata.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

# Iterate through the imported data
for item in data:
	print(item)
