import re
def func():
      print("your password should be atleast 8 charctres")
      print("password should contain charcters like @#$&")
      print("password should should contain lowercase and uppercase charcters ")
pattern=re.compile(r'[a-zA-Z0-9@#$&]{8,}\d')
while True:
      
      password=input('genrate your password')
      try:  
            if pattern.fullmatch(password):
                  print('your password has been generated')
                  break
            else:
                  password=bool(password)
                  raise EnvironmentError
      except Exception as e:
            print('error is ',e)
            func()



patt=re.compile(r"[a-z]")       

with open("test.txt","r") as f:
      for line in f:
        stri=patt.finditer(line)
        for s in stri:
            print(s)


