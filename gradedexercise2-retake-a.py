import pandas as pd # Import pandas module

data = pd.read_csv('http://www.cedriccourtois.be/files/articletitles.csv',sep=';') # Read datafile
data = data.T.to_dict().values() # Convert to list of dictionaries 

count = 0 # Set counter to 0 (starting value)

for item in data: # Loop through list of dictionaries
  item['TitleLower'] = item['Title'].lower() # Add key 'TitleLower' with a value that equals to the lowercase version of the iteration value for the key 'Title'
  if 'covid' in item['TitleLower'] or 'corona' in item['TitleLower']: # Check whether 'covid' is in the iteration value of 'TitleLower' (defined on line 9) or 'corona' is in that iteation value
    count += 1 # If the conditional is true, one unit is added to the counter (only in that case)

print(count) # Print final value of count, as the loop was is termined (i.e., no indentation)
