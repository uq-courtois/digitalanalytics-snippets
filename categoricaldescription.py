import pandas as pd
import researchpy as rp

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

pd.set_option('max_rows', 9999) # Set minimum of rows to show, in/decrease to needs

### Mode, frequencies, counts of categorical variable
print(rp.summary_cat(df['productionlocation'])) 

# > Mode is value with highest count: 'USA'
# > Counts are absolute frequencies
# > Percentages are relative frequencies

print()

### Median of any variable (i.e., middle value when ordered)
print('Median:',(df['year']).median())
