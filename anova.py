import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from pingouin import welch_anova

df = pd.csv('http://www.digitalanalytics.id.au/static/files/imdb_data_clean.csv', delimiter = ',') 

### BAR PLOTS OF THREE GROUPS FOR A VARIABLE

# Subset three groups
group1 = df[df['productionlocation']=='USA']['rating']
group2 = df[df['productionlocation']=='Coproduction']['rating']
group3 = df[df['productionlocation']=='Non-USA']['rating']

means = (group1.mean(),group2.mean(),group3.mean()) # Calculating means
positions = [0, 1,2] # Defining positions in the graph
plt.bar(positions, means) # Compiling the plot
plt.xticks(positions,['USA', 'Coproduction','Non-USA'],rotation="horizontal") # Adding labels
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig("barmeanstd3+.pdf") # Save figure
plt.clf() # Clear figure

# Get descriptive table by category
print(rp.summary_cont(df['rating'].groupby(df['productionlocation'])))
pd.set_option('max_columns', 9999)

# Welch's ANOVA
aov = welch_anova(dv='rating', between='productionlocation', data=df)
print(aov)
