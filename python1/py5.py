



try:
   def armstrong(x):
      for i in x:
          if int(i)//2==0:
              yield int(i)
          z=0
          if int(i)//2==5:
             for j in i:
                z=z+int(j)*int(j)
             yield z        
          b=0
          if int(i)//2==50:
             for j in i:
                b=b+int(j)*int(j)*int(j)
             yield b
   a=[str(i) for i in range(1000)]
   print(list(armstrong(a))) 


except Exception as e:
    print("there is error ",e)



#occcurance of a sequance
a=[2,5,3,6,5,2,6]
x=min(a)
print(a.index(x))
dic={}
a=[2,5,3,6,5,2,6]
# dic={k:v for k,v in map(enumerate,a)}
for k in a:
    print(k)
    dic[k]=dic.get(k,0)+1
print(dic)

def res(d,e):
   temp=d
   d=e
   e=temp
   return d,e

print(res(5,3))