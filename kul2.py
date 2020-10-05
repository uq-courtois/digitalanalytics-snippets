### Exercise 1

#1 Read data from the file articletitles.csv with two variables: Title and URL (Download the file from http://www.cedriccourtois.be/files/articletitles.csv) and convert into a list of dictionaries
#2 Add a new key called TitleLower to your list of dictionaries. The value should be the value of Title converted into lowercase (use the .lower() method, e.g., to convert a variable 'Var' into lowercase, you use Var = Var.lower()
#3 Indicate whether the lowercase conversion of the title contains 'covid' or 'corona' (possible values are 'Yes' or 'No' - This will be another added key, called CoronaMention)
#4 Write a new file articletitles_processed.csv with four variables: Title, TitleLower,  URL, CoronaMention

### Exercise 2

#1 Read the data from the file diameters.csv (http://www.cedriccourtois.be/files/diameters.csv)
#2 Calculate the circumference of a circle based on the given diameter values (formula: pi * diameter. Remember: pi = 3.14) and add that value in a key 'circumference’
#3 Print the observationids of all circles with a circumference larger than 10
#4 Write a new file with the observationids, the diameters, and the circumference as variables. Name the file circles.csv
