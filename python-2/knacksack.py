#maxprofit

t=int(input("no of test cases"))

def knacksack(wgs,pt,wg,n,dic={}):
    key="{} {}".format(wg,n)
    if key in dic:
        return dic.get(key)
    if wg==0 or n==0:
        return dic

    elif wgs[n-1]>wg:
        return knacksack(wgs,pt,wg,n-1,dic)

    else:
        dic[key]=max(knacksack(wgs,pt,wg,n-1,dic),(knacksack(wgs,pt,wg-wgs[n],n-1,dic)+pt[n-1]))

for j in range(t):
   wg=int(input("wt of bag")) 
   wgs=list(map(int,input().split()))
   pt=list(map(int,input().split()))
   knacksack(wgs,pt,wg,len(wgs))

