import requests
payload={'gl':"IN"}
res=requests.get('https://www.google.com/webhp',params=payload)
text=res.text
print(text)
lis=[]
# with open("response.json","w") as f:
#      f.write(text)
# lis.append(text)

print(res.status_code)
print(res.headers['Content-type'])

