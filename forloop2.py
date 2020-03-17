numbers = [4,3,5,4,6]

for item in numbers:
  print(item*5)
  
# Output:
# 20
# 15
# 25
# 20
# 30

# Note: each element, without exception is multiplied by 5 and printed

names = ['Eric','Wang','Lisa']

for item in names:
  if 'a' in item:
    print(item)
    
# Output:
# Wang
# Lisa

# Note: only values of the iteration variable 'item' with an 'a' in it are printed. 
# This is because the code in the for loop contains a conditional that requires an 'a'
# to execute the code it wraps, which is the print-statement.
# During the first iteration, item will contain the value 'Eric', but nothing
# is done with it because there is no particular instruction. The iteration will
# just pass and move on to Wang, which does contain an 'a', and will be printed.
