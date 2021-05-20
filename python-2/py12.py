from PIL import Image

import os
os.chdir('c:/Users/Public/Pictures/Sample Pictures')
i=1
for f in os.listdir():
    if f.endswith('.jpg'):
        image=Image.open(f)
        # fil,extension=os.path.splitext(f)
        
        
        image.save('pngs/{}{}.png'.format(i,'new'))
        i=i+1