t=input("enter")
t=int(t)
 
while(t>0):
    
    
    li=list(map(int,list(input("ent").split())))
    mi=li.index(min(li))
    di=(len(li)-1)-mi
    sum=0
    div=di*min(li)+min(li)
    for i in range(0,mi):
        sum=sum+li[i]
        print(sum)
    t=t-1    
    print(div+sum)    