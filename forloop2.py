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
names_with_a = []

for item in names:
  if 'a' in item:
    names_with_a.append(item)
print(names_with_a)                
                        
# Output:
# ['Wang','Lisa']

# Note: the for loop will iterate through all three names, one by one:
# Iteration 1: Eric
# Iteration 2: Wang
# Iteration 3: Lisa

# When there is an 'a' in the value of item (conditional on line 19), 
# the program will append the value of 'item' to the originally empty list.

# Iteration 1: Eric > conditional is False, code wrapped in if-statement is
# ignored and the program moves to second iteration

# Iteration 2: Wang > condition is True, code wrapped in the if-statement is executed:
# the value of iteration variable 'item' 'Wang' is added to the empty list 'names_with_a',
# and the program moves to the third iteration

# Iteration 3: Lisa > condition is True, code wrapped in the if-statement is executed:
# the value of iteration variable item 'Lisa' is added to the list 'names_with_a', which
# up until then only contains the value 'Wang' (added in the second iteration)

# After iteration 3, the for loop is termined because all elements are looped through
# We return to the original indentation level and print 'names_with_a'
# The last contents of 'names_with_a' (i.e., at the end of the third and final iteration)
# are printed to the console


# At the end of the for loop, two values will have been added: Wang and Lisa


