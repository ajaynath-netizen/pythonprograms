from PIL import Image
import os

os.chdir("C:/Users/amarnath/Documents")
c=1
for pic in os.listdir():
  if pic.endswith('jpg'):
    image=Image.open(pic)
    a,b=image.size
    print(a,b)
    if b>=1000:
       image.resize((9444,563),Image.ANTIALIAS)
    else:

       image.resize((200,370),Image.ANTIALIAS)
    # print(image.size)
    if not os.path.exists('mine'):
       os.mkdir('mine')
    image.save("mine/{}.jpg".format(c),quality=55,optimize=True)
    c=c+1
