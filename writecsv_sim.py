# WRITING DATA TO CSV
newdata = pd.DataFrame(variable_name)  # Converting list of dictionaries into dataframe
newdata.to_csv('newdatafile.csv', sep=',', index=False)  # Writing dataframe into CSV file

# Make sure pandas is imported at the top of your script if you don't already have it
# The variable variable_name is where the data that you want to write is stored in your script, change this as needed
