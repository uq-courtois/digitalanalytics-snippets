lista = ['Lisa','Erik','Jean','Omar','David','Michael']
listb = ['David','Jing','Amina','Michael']
 
# We want to find and print the names both lists have in common.
 
for namea in lista: # OUTER LOOP
   
  for nameb in listb: # INNER LOOP
  
    if namea == nameb: # adding a condition to only show exact matches
      print(namea,nameb)
      
     # Output:
     # David David
     # Michael Michael
     # These are the two names that are shared by both lists
