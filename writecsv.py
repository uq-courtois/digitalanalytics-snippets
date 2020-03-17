# New data, hardcoded into our script:
newdata = [
        {'Course':'Maths','Grade':'14'},
        {'Course':'French','Grade':'16'},
        {'Course':'Physical Exercise','Grade':'12'},
        ]

# Create a new CSV file, called newfile.csv:
csv_file = open('newfile.csv','a') # Open a new file, called imdprocessed.csv, allow to append information
csv_writer = csv.writer(csv_file, delimiter=';') # Define csv writer, set the delimiter
csv_writer.writerow(['Course','Grade']) # Write the first row, containing variable names - DO THIS ONLY ONCE...
csv_file.close # Close file

for item in newdata: # To write into the CSV, row by row...
  csv_file = open('newfile.csv','a') # Open file, allow to append
  csv_writer = csv.writer(csv_file, delimiter=';') # Not necessary, but reset delimiter just to be sure...
  csv_writer.writerow([
                         item['Course'],
                         item['Grade'],
                         ]) # Write result row, based on the two keys in each dictionary
  csv_file.flush() # Force to flush
  csv_file.close # Close file
