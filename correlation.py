import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 
print(df.info())

### CORRELATION
print(rp.correlation.corr_pair(df[['agefilm', 'rating']]))

# The r-value is the magnitude of the correlation
# p-value expresses statistical significance level
# N reports number of cases the analysis is based on

### SCATTERPLOT
plt.scatter(df['agefilm'],df['rating']) # Build plot
plt.xlabel('Year of release') # x-axis label
plt.ylabel('IMDB user rating') # y-axis label
plt.savefig('scatterplot.pdf') # Save figure
plt.clf() # Clear figure
