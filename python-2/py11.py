import json
try:
   with open('C:/Users/amarnath/source/repos/WebApplication1/WebApplication1/obj/project.assets.json','r') as f:
      x=json.loads(f)
    
    #   jso=json.dumps(x)
      print(x)
except Exception as e:
    print('error is',e)

obj = ''' {
    "name":"ajay",
    "email":"ajay@gmail.com",
    "phone":9618035625,
    "hobbies":["coding","writing","reading","walking","watching"],
    "ob":{
        "a":10,
        "b":20,
        "c":30
    }
} 
'''
try:
  a=json.loads(obj)
  print(a.get('hobbies',0))
  
  print(a.values())
except Exception as e:
   print(e,"error")



a=[chr(i) for i in range(97,123)]
print(a)