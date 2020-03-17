# Goal of this program is to filter all string values from a list
# named originallist and store them in a new list named stringlist
# At the end, the contents of the variable stringlist should be printed
# just once. Correct the program so it does that, and only that...

originallist = [4,3,'Erik',5,4,'Johanna',3,1,'Marcela']
stringlist = []

for item in originallist:
	if type(item) == str:
		stringlist.append(item)
		print(stringlist)
