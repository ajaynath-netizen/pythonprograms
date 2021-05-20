# def inputs(take):
#     def wrap(k,v):
#         stri=input("enter word to be {}".format(choice))
#         key=int(input("enter key"))
#         take(stri,key)
#     return wrap

# def fun(choice):
#     if choice=="encrypt":
        
def encrypt(k,v):
 try:
    a=[chr(i) for j in range(10) for i in range(97,123)]
    st=""
    for i in k:
        index=a.index(i)
        # if index+v>=28:
        #     index=0

        # else:

        st=st+a[index+v]
    return st
        # return inputs(encrypt)(k,v)
    # else:
    #     @inputs
 except Exception as e:
     print(e)  

def decrypt(k,v):
  try:
    a=[chr(i) for i in range(97,123)]
    st=""
    for i in k:
        index=a.index(i)
        st=st+a[index-v]
    return st
  except Exception as e:
      print(e)

def source(x):
    dic={"encrypt":encrypt,"decrypt":decrypt}
    c=dic.get(x)
    return c

def select():
    print("encrypt -> for encryption")
    print()
    print("decrept -> for decryption")
    print()
    print("3 -> to get back")

    while True:
      try:
        choice=input("select from above : ").lower()
        stri=input("enter word to be {}".format(choice)).lower()
        key=int(input("enter key : "))

        if choice=="encrypt" or choice=="decrypt":
             return source(choice)(stri,key)

        elif choice==str(3):
            select()
      
      except:
          print("enter valid inputs")
          select()

print(select())