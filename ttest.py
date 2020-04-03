import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

### BOX PLOTS OF TWO GROUPS FOR A VARIABLE

# Subset two groups
l_sfx = df[df['sfxgenre']=='lower sfx']['rating']
h_hsfx = df[df['sfxgenre']=='higher sfx']['rating']
# Plot the data
plt.boxplot([l_sfx,h_hsfx])
# Add labels
plt.xticks([1, 2], ['Low SFX', 'High SFX'])
# Save plot
plt.savefig('boxplot.pdf')
# Clear figure
plt.clf()

# Calculate and print Welch’s t-test
print(stats.ttest_ind(l_sfx, h_hsfx, equal_var = False))
