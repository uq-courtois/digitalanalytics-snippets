import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/imdb_data_clean.csv', delimiter = ',') 

# Set max of rows to show, in/decrease to needs
pd.set_option('max_rows', 9999) 

# CROSSTABULATION
table, results = rp.crosstab(df['sfxgenre'],df['productionlocation'], prop= 'col', test= 'chi-square')

print(table) # Prints crosstab
print()
print(results) # Prints statistics tab

# STACKED BAR CHART
ct = pd.crosstab(df['productionlocation'],df['sfxgenre'],normalize='index') # Create PD crosstab as basis for plot
ct.plot.bar(stacked=True) # Generate plot
plt.legend(loc='lower left', bbox_to_anchor= (0.0, 1.01),frameon=False) # Tidy up legend (other)
plt.xticks(rotation="horizontal") # Horizontal x-axis labels
plt.xlabel('Production location') # Adding label on x-axis
plt.ylabel('Proportion SFX') # Adding label on y-axis
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig('stackedbar.pdf') # Saving figure

# Clear figure
plt.clf() 
