import random



password=input("enter password")
x= 12345
count=1
while True:
    try:


      if password=="password":

            print("u r near")
            print("try again")
            break

      elif x==int(password):
            print("u r in")
            break
          
    except:
         if count<=3:
            print("invalid password")
            password=input("enter a correct password")
            count=count+1
         else:
               break
          
