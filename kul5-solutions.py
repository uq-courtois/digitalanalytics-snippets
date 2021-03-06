import pandas as pd

# 1. Read the data file from http://cedriccourtois.be/files/youtube_vevo.csv

df = pd.read_csv('http://cedriccourtois.be/files/youtube_vevo.csv', delimiter = ';') # Import data

# 2. Remove exact duplicates from the loaded dataframe

df = df.drop_duplicates() # Drop exact duplicates

# 3. Create a new variable in the dataframe that only contains the year of publication

df['year'] = df['published'].str[-4:] # Retaining a specific range

# 4. Create a new variable that marks video’s with less than 1 million views with a value 0, and video’s with 1 million or more views as a 1.

df['viewsover1m'] = df['views'].apply(lambda x: 0 if x < 1000000 else 1)

print(df[['published','year','views','viewsover1m']]) # To check...

# 5. Save the dataframe in a new csv file named youtube_vevo_cleaned.csv

df.to_csv(r'youtube_vevo_cleaned.csv', sep = ';') # Save processed version of data file

# 6. Views MEAN, STANDARD DEVIATION (std), MEDIAN (50%)
print(df['views'].describe())

# 7. CORRELATION views-likes, views-dislikes
print(rp.correlation.corr_pair(df[['views', 'likes']]))
print(rp.correlation.corr_pair(df[['views', 'dislikes']]))
 
# 8. SCATTERPLOT views-likes, views-dislikes

plt.scatter(df['views'],df['likes']) # Build plot
plt.xlabel('Number of views') # x-axis label
plt.ylabel('Number of likes') # y-axis label
plt.savefig('scatterplot1.pdf') # Save figure
plt.clf() # Clear figure

plt.scatter(df['views'],df['dislikes']) # Build plot
plt.xlabel('Number of views') # x-axis label
plt.ylabel('Number of dislikes') # y-axis label
plt.savefig('scatterplot2.pdf') # Save figure
plt.clf() # Clear figure


