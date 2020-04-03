import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from pingouin import welch_anova, read_dataset

df = pd.read_csv('imdb_data_clean.csv', delimiter = ';') 

### BAR PLOTS OF THREE GROUPS FOR A VARIABLE

# Subset three groups
usa = df[df['productionlocation']=='USA']['rating']
coprod = df[df['productionlocation']=='Coproduction']['rating']
nonusa = df[df['productionlocation']=='Non-USA']['rating']

means = (usa.mean(),coprod.mean(),nonusa.mean()) # Calculating means
std = (usa.std(),coprod.std(),nonusa.std()) # Calculating standard deviations
positions = [0, 1,2] # Defining positions in the graph
plt.bar(positions, means, yerr=std) # Compiling the plot
plt.xticks(positions,['USA', 'Coproduction','Non-USA'],rotation="horizontal") # Adding labels
plt.savefig("barmeanstd3+.pdf") # Save figure
plt.clf() # Clear figure

# Get descriptive table by category
print(rp.summary_cont(df['rating'].groupby(df['productionlocation'])))

# Welch's ANOVA
aov = welch_anova(dv='rating', between='productionlocation', data=df)
print(aov)
