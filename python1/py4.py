
import time

def seti(func):
   
   def wrap():
     k=0
     while k<=5:
        print(k)
        x=time.time()
        func()
        y=time.time()-x
        print(y)
        k=k+1
        
   return wrap


def repeat():
    
  for j in range(5):

     for i in range(j+1):

       print(i+1, end=" ")
      
     print()
     j=j+1

seti(repeat)()




















    