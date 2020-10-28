# You probably know Vevo, an entertainment video service that is a joint venture between Sony, EMI and Universal. It has a dominant presence on YouTube, where it provides access to branded artist channels. In this exercise, you will work with data scraped from its main YouTube channel. Data were scraped on the channel’s video’s posted in the past ten years: (a) title, (b) nuber of views, (c) published date, (d) number of likes, (e) number of dislikes, and (d) the url (i.e., the unique video id).

# Write a script following these steps:
# Read the data file from http://cedriccourtois.be/files/youtube_vevo.csv
# Create a new variable in the dataframe that only contains the year of publication
# Create a new variable that marks video’s with less than 1 million views with a value 0, and video’s with 1 million or more views as a 1.

# Print an output that contains the mean, standard deviation, and median of the variable views.
# Consider the two variable pairs:
# - The number of views and likes
# - The number of views and dislikes
# Test the relationships between both variable pairs, so (a) number views - likes and (b) number views - dislikes, using a single statistic. There should be one statistic per relationship.
# Plot the relationships between these two variable pairs (so generate two plots with different file names - don't forget to clear the image definitions in your code each time right after saving them... >>> plt.clf()
