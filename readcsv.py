import csv # We need to call this module

file = open('csvtutorial.csv', 'r') # CSV file 'csvtutorial' in the same path as our Python script is opened

importdata = csv.DictReader(file, delimiter=',') # File contents written into list of dictionaries named 'importdata'
# Note that the delimiter is a comma. Always check what delimiter your CSV file uses. I might as well be a semi-colon ';'

for item in importdata: # We loop through the data to get a grasp of it and/or to process/manipulate it further...
    print(item['Name'],'is',item['Age'],'years old')
