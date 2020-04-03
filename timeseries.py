import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from pingouin import welch_anova, read_dataset

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

### Displaying time series

# Calculate mean, minimum, and maximum ratings per year (groupby)
ymean = df.groupby('year', as_index=False)['rating'].mean()
ymdn = df.groupby('year', as_index=False)['rating'].median()
ymin = df.groupby('year', as_index=False)['rating'].min()
ymax = df.groupby('year', as_index=False)['rating'].max()

# Plot these variables together
plt.plot(ymin['year'],ymin['rating'],label="Minimum rating")
plt.plot(ymean['year'],ymean['rating'],label="Average rating")
plt.plot(ymdn['year'],ymdn['rating'],label="Median rating")
plt.plot(ymax['year'],ymax['rating'],label="Maximum rating")

# Add a legend
plt.legend()
# Save the figure
plt.savefig('timeseries.pdf')
