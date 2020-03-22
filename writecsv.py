### WRITING

# Import pandas
import pandas as pd

# New data, hardcoded into our script:

newdata = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]

newdata = pd.DataFrame(newdata) # Converting list of dictionaries into dataframe
newdata.to_csv('newdata.csv',sep=';',index=False) # Writing dataframe into CSV file
