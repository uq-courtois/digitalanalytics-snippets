number = 0

while number < 5: # As long as the value of number is smaller than 5, the loop continues)
  print(number) # We print the current value of number at the beginning of each loop
  number = number + 1 # We add one to the current value of number at the end of each loop
  
print("Loop ended. Final value of 'number' is",number)

# Output:
# 0 > (Iteration 1: number = 0 when it is printed on line 4, right after, we add one on line 5)
# 1 > (Iteration 2: number = 1 when it is printed on line 4, right after, we add one on line 5)
# 2 > (Iteration 3: number = 2 when it is printed on line 4, right after, we add one on line 5)
# 3 > (Iteration 4: number = 3 when it is printed on line 4, right after, we add one on line 5)
# 4 > (Iteration 5: number = 4 when it is printed on line 4, right after, we add one on line 5)

# After the fifth iteration, the condition is no longer True because the value of number is
# increased to 5 at the end of the fifth iteration. The statemetn 5 < 5 is False, so the
# while loop is terminated and we move on to the print statement at line 7, which will output:
# "Loop ended. Final value of 'number' is 5".
