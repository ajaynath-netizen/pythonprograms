import zipfile
import os
# with zipfile.ZipFile("C:/Users/amarnath/Documents/10128_1434247_bundle_archive.zip","r") as file:
os.chdir('C:/Users/Public/Pictures/Sample Pictures')
with zipfile.ZipFile('fil.zip','w',compression=zipfile.ZIP_DEFLATED) as f:
      for pic in os.listdir():
    
         if pic.endswith('jpg'):

            print(pic)
            f.write(pic)

with zipfile.ZipFile('fil.zip','r') as p:
   p.extractall('app')


with zipfile.ZipFile("C:/Users/amarnath/Documents/archive.zip","r") as file:
   file.extractall('C:/Users/amarnath/Documents/dataset')

# for f in os.listdir('fil.zip'):
#    print(f)


print(os.getcwd())
      
