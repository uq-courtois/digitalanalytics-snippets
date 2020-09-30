### Exercise 1

listx = [5,9,5,6,7,8]
listx.sort(reverse=True)
#listx.reverse()
listx.append(7)
varx = listx[-1]
print(varx*10)
print(listx)

### Exercise 2

listx = [5,9,5,6,7,8]
listy = []

for item in listx:
	print(item/2)
	listy.append(item/2)

print('The divided numbers are:',listy)

### Exercise 3

names = ['lisa','john','peter','lisa','marc']

while 'lisa' in names:
	names.remove('lisa')

### Exercise 4

length = 2
width = 4
height = 3

volume = length * width * height

print('The cuboid has a volume of',volume,'cubic meters')

### Exercise 5

### Exercise 5

quotes = [
'The ancients dreaded death: the Christian can only fear dying. (Augustus William Hare)',
'We who engage in nonviolent direct action are not the creators of tension. We merely bring to the surface the hidden tension that is already alive. (Martin Luther King)',
'I have criticized absent people so often, and then discovered, to my humiliation, that I was talking with their relatives, that I have grown superstitious about that sort of thing and dropped it. (Mark Twain)',
'The injury that we do to a man must be such that we need not fear his vengeance (Steve Perry)'
]

for quote in quotes:
	if 'we' in quote.lower():
		print(quote)
