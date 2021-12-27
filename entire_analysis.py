import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats

# Read the data
df = pd.read_csv('http://www.digitalanalytics.id.au/static/files/imdb_data_clean.csv', delimiter = ',')

# Descriptives of Age (i.e., how old a series is, for sample description)
df['Age'] = 2021 - df['Year']
print(df['Age'].describe())

# Descriptives of imdbRating (for measures section)
print(df['imdbRating'].describe())

# Descriptives of english (for measures section)
catsum = rp.summary_cat(df['english'])
print(catsum)

# Descriptives of productionlocation (for measures section)
catsum = rp.summary_cat(df['productionlocation'])
print(catsum) 

# Language t-test + visualisation

# Subset two groups
group1 = df[df['english']=='yes']['imdbRating']
group2 = df[df['english']=='no']['imdbRating']
print('Group means:',round(group1.mean(),2),round(group2.mean(),2))
print('Group stds:',round(group1.std(),2),round(group2.std(),2))
 
degreesoffreedom = (len(group1)+len(group2)-2)
print('Degrees of freedom',degreesoffreedom)
 
means = (group1.mean(),group2.mean()) # Calculating means
positions = [0, 1] #Defining positions in the graph
plt.bar(positions, means) # Compiling the plot
plt.xticks(positions,['English', 'Non-English'],rotation="horizontal") # Adding labels
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig("barmean_english.pdf") # Save figure
plt.clf() # Clear figure
 
# Calculate and print Welch’s t-test
print(stats.ttest_ind(group1, group2, equal_var = False))

# Location t-test + visualisation
group1 = df[df['productionlocation']=='USA only']['imdbRating']
group2 = df[df['productionlocation']=='Non-USA']['imdbRating']
print('Group means:',round(group1.mean(),2),round(group2.mean(),2))
print('Group stds:',round(group1.std(),2),round(group2.std(),2))
 
degreesoffreedom = (len(group1)+len(group2)-2)
print('Degrees of freedom',degreesoffreedom)
 
means = (group1.mean(),group2.mean()) # Calculating means
positions = [0, 1] #Defining positions in the graph
plt.bar(positions, means) # Compiling the plot
plt.xticks(positions,['USA', 'Non-USA'],rotation="horizontal") # Adding labels
plt.tight_layout() # Forces tidy plot lay-out
plt.savefig("barmean_productionlocation.pdf") # Save figure
plt.clf() # Clear figure
 
# Calculate and print Welch’s t-test
print(stats.ttest_ind(group1, group2, equal_var = False))
