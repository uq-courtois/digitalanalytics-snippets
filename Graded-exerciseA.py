### Read data from the file observationsC.csv with two variables: ObervationID and DegreecCelcius (Download the file from http://www.cedriccourtois.be/files/observationsC.csv) and convert into a list of dictionaries

# Code adapted from Module 2: Read data

import pandas as pd

data = pd.read_csv('http://www.cedriccourtois.be/files/observationsC.csv',sep=';') # Reading data from csv
data = data.T.to_dict().values() # Converting dataframe into list of dictionaries

for item in data: # Not necessary, but temporarily helpful to check whether everthing worked, and to get to know the data
	print(item)

### Convert the temperatures in °C (which by now is a key in the list of dictionaries you are working with) to °F (i.e., a new key named DegreeFahrenheit). The conversion formula is >>> (°C * 9/5) + 32 = °F

# Code adapted from Module 1: Exercise 11 on for loops - We're adding a key there as well, based on existing key-value data

for item in data:
  item['DegreeFahrenheit'] = (item['DegreecCelcius'] * 9/5) + 32 # Adding the key DegreeFahrenheit to each dictionary, based on given formula that includes the value of 'DegreecCelcius'

  ### Indicate whether the temperature is equal to or exceeds a threshold temperature of 30°C (possible values are 'Yes' or 'No', written into a new key 'TresholdExceeded')

  # Code adapted from Module 1: Conditionals

  if item['DegreecCelcius'] >= 30:
    item['ThresholdExceeded'] = 'Yes'
  else:
    item['ThresholdExceeded'] = 'No'

### Write a new file observationsCF.csv with four variables: ObervationID, DegreeCelcius, DegreeFahrenheit, TresholdExceeded

# Code adapted from Module 2: Write data

data = pd.DataFrame(data) # Converting list of dictionaries into dataframe
data.to_csv('observationsCF.csv',sep=';',index=False) # Writing dataframe into CSV file

# Tip: Always check whether your output data make sense: open the file, eyeball it...
