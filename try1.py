dataset = [
	{'name':'Marc','age':26},
	{'name':'Jane'},
	{'name':'Lisa','age':23},
]

for item in dataset:
  try:
    print(item['name'],item['age'])
  except:
    pass
