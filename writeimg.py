from urllib.request import Request, urlopen

imgurl = "https://i.scdn.co/image/62b33d12e2b9a033cf77585f6e3d4b2c6b3a63a1"

imgfile = open('image.jpg','wb') # Create a new, empty picture file
imgfile.write(urlopen(imgurl).read()) # Write picture information into empty file
imgfile.close() # Close file
