import pandas as pd # To handle/analyse data
import researchpy as rp # To generate concise tables
import matplotlib.pyplot as plt # To create visualisations

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

pd.set_option('max_rows', 9999) # Set minimum of rows to show, in/decrease to needs

### MODE, FREQUENCIES, AND COUNTS
catsum = rp.summary_cat(df['productionlocation'])
print(catsum)
# Mode is value with highest count: 'USA'
# Counts are absolute frequencies
# Percentages are relative frequencies

### BART CHART
plt.bar(catsum['Outcome'],catsum['Count'])
# x-labels based on outcome strings of catsum
# bar height based on count figures of catsum

# Saving the image to a file
plt.savefig('productionlocation-barchart.pdf')

# For extensive customisation options of bar charts in plt: see https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.bar.html

print()

### Median of any variable (i.e., middle value when ordered)
print('Median:',(df['year']).median())
