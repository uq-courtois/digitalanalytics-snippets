def calculation(number):
	number = number * 5
	return number

number = 5 # Value of number is set to 5
print(calculation(number)) # We feed value of number (i.e., 5) into function and print the returned result (i.e., 25)

# Some other code...

number = 6
print(calculation(number)) # We feed value of number (i.e., 6) into function and print the returned result (i.e., 30)

# Yet some other code

number = 9
print(calculation(number)) # We feed value of number (i.e., 9) into function and print the returned result (i.e., 45)

# Output:
# 25
# 30
# 45

# If we change the calculation to add 5, this requires only on change on line 2 (i.e., changing * to +)
# In this example, the instruction is simple and does not
# really save space, but it would if the calculation would
# be more complicated and hence require more lines of code
