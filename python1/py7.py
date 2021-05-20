lis=[]
i=0
while True:
        
        try:
           x=input("enter your {0} number".format(i))
           lis.append(int(x))
           print("type enough to exit if no more numbers")
           i=i+1
           


        except:
        
            if x=="enough":
              break

def addi(lis):
    sum=0

    for i in lis:
        sum =sum+i
    return sum
def mult(lis):
    mul=1
    for i in lis:
        mul=mul*i
    return mul
def div(lis):
    div=1
    for i in lis:
        div=i/div
    return div

def calculator():
    print("1 : addition")
    print("2 : substraction")
    print("3 : multiplication")
    print("4 : division")
    print("5 : square")

    while True:
      y=input("choose 1/2/3/4/5 from above list")
      try:
         if int(y)==1:
           print(addi(lis))
           print("enter 6 to go back")

    
         if int(y)==3:
            print(mult(lis))
            print("enter 6 to go back")

         if int(y)==4:
             print(div(lis))
             print("enter 6 to go back")

         if y or int(y) not in (1,3,4):
             print("enter valid number")

         if int(y)==6:
            calculator()

      except:
         print("come again")
         if y=="quit":
            break
calculator()
    

    