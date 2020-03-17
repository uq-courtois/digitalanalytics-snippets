# Goal of this program is to filter all string values from a list
# At the end, the contents of the variable stringlist should be printed
# Correct the program so it does just that...

originallist = [4,3,'Erik',5,4,'Johanna',3,1,'Marcela']
stringlist = []

for item in originallist:
	if type(item) == str:
		stringlist.append(item)
		print(stringlist)
