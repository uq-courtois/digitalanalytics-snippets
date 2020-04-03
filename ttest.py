import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

### BOX PLOTS OF TWO GROUPS FOR A VARIABLE

# Subset two groups
l_sfx = df[df['sfxgenre']=='lower sfx']['rating']
h_sfx = df[df['sfxgenre']=='higher sfx']['rating']

means = (l_sfx.mean(),h_sfx.mean()) # Calculating means
std = (l_sfx.std(),h_sfx.std()) # Calculating standard deviations
positions = [0, 1] #Defining positions in the graph
plt.bar(positions, means, yerr=std) # Compiling the plot
plt.xticks(positions,['Low SFX', 'High SFX'],rotation="horizontal") # Adding labels
plt.savefig("barmeanstd.pdf") # Save figure
plt.clf() # Clear figure

# Calculate and print Welch’s t-test
print(stats.ttest_ind(l_sfx, h_sfx, equal_var = False))
