import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

pd.set_option('max_rows', 9999) # Set minimum of rows to show, in/decrease to needs

### MEAN, STANDARD DEVIATION (std), MEDIAN (50%)
print(df['duration'].describe())

### HISTOGRAM
# Render histogram (By increasing the bins number, you smoothen the graph)
plt.hist(df['duration'], bins=100)

# Save figure as pdf
plt.savefig('histo_duration.pdf')

plt.clf() # Clear figure
