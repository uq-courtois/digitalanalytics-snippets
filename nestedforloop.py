lista = ['Lisa','Erik','Jean','Omar','David','Michael']
listb = ['David','Jing','Amina','Michael']

# We want to find and print the names both lists have in common.

for namea in lista: # OUTER LOOP

  # We start by looping through lista, this is the outer loop.
  # This will go through all the names in lista, one by one
  
  for nameb in listb: # INNER LOOP
  
  # By starting a second loop within the first loop. This is the inner loop
  # We will go through each name of the listb per iteration (!!!) of the outer loop
  
    print(namea,nameb)
    
    # This will provide the following output, which are all the possible combinations:
    
    # Lisa David (First iteration outer loop, first iteration inner loop)
    # Lisa Jing (First iteration outer loop, second iteration inner loop)
    # Lisa Amina (First iteration outer loop, third iteration inner loop)
    # Lisa Michael (First iteration outer loop, fourth iteration inner loop)
    # Erik David (Second iteration outer loop, first iteration inner loop)
    # Erik Jing (Second iteration outer loop, second iteration inner loop)
    # Erik Amina (Second iteration outer loop, third iteration inner loop)
    # Erik Michael (Second iteration outer loop, fourth iteration inner loop)
    # Jean David ...
    # Jean Jing
    # Jean Amina
    # Jean Michael
    # Omar David
    # Omar Jing
    # Omar Amina
    # Omar Michael
    # David David
    # David Jing
    # David Amina
    # David Michael
    # Michael David
    # Michael Jing
    # Michael Amina
    # Michael Michael
