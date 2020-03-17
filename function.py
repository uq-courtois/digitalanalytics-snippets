def calculation(number):
	number = number * 5
	return number

number = 5
print(calculation(number))

# Some other code...

number = 6
print(calculation(number))

# Yet some other code

number = 9
print(calculation(number))

# Output:
# 25
# 30
# 45

# If we change the calculation to add 5, this requires only on change on line 2 (i.e., changing * to +)
# In this example, the instruction is simple and does not
# really save space, but it would if the calculation would
# be more complicated and hence require more lines of code
