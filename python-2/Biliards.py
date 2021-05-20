def no_ways(sum,dic={}):
    
    if su in dic.values():
        return dic.get(su)
    
    
    if su<=1:
     
     return 0
     
    if su==2 or su==3: 
     
     return 1
     
    
     
    dic[sum]=no_ways(su-2,dic) + no_ways(su-3,dic)
    
    
# your code goes here
t=input("cases")

for i in range(int(t)):
    
    su=int(input("sum")) 
    print(no_ways(su))