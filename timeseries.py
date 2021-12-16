import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/imdb_data_clean.csv', delimiter = ',') 

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

# Forces tidy plot lay-out
plt.tight_layout()

# Save the figure
plt.savefig('timeseries.pdf')

# Clear figure
plt.clf()
