# WRITING DATA TO CSV
newdata = pd.DataFrame(newdata)  # Converting list of dictionaries into dataframe
newdata.to_csv('newdatafile.csv', sep=',', index=False)  # Writing dataframe into CSV file

# ! Make sure pandas is imported at the top of your script if you don't already have it
