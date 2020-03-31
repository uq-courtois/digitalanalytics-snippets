for item in data:
   item['TitleLower']=item['Title'].lower()

   if 'covid'in TitleLower or 'corona'in TitleLower:
        item['CoronaMention']='Yes'
   else:
        item['CoronaMention']='No'
   print(item)
