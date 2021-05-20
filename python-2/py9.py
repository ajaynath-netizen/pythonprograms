with open('./test.txt','w') as f:
    
    f.write('1.rayudu is best \n2.rohit is best')
    f.write('\n3.dhoni is best')
    
f=open('test.txt','r') 

for line in f:

   x=line.rstrip()
  
   print(x)
f.close()


    
import os

print(os.stat('test.txt').st_size)
print(os.getcwd())

for dirpath, dirnames,filenames in os.walk('c:/Users/Amarnath/Documents'):


  print("curren path:",dirpath)
  for f in os.listdir(dirpath):
      if "." in f:
         print(os.path.splitext(f))
         print()
      else:
        print(f)
         
  # print("directris:",dirnames)
  # print("filename:",filenames)


os.chdir('C:/Users/Public/Music/Sample Music')

for f in os.listdir():
      
      print(os.path.splitext(f))
      
print(os.getcwd())






