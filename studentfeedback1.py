for item in data:
   item['TitleLower']=item['Title'].lower()

   if 'covid' in item['TitleLower'] or 'corona' in item['TitleLower']:
        item['CoronaMention']='Yes'
   else:
        item['CoronaMention']='No'
   print(item)
