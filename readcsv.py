import csv # We need to call this module

file = open('csvtutorial.csv', 'r') # CSV file 'csvtutorial' in the same path as our Python script is opened

importdata = csv.DictReader(file, delimiter=';') # Filecontents written into list of dictionaries names importdata

for item in importdata: # We loop through the data to get a grasp of it and/or to process/manipulate it further...
    print(item['Name'],'is',item['Age'],'years old')
