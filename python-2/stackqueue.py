class stack:
    
    def __init__(self,a):
        
        self.a=a
    def push(self,var):
        x= self.a.append(var)
        print(x)
        return x
        
    def pop(self):
        if len(self.a)>0:
          return self.a.pop()
        else:
            return len(self.a)<0
c=[5,8,6,3]
b=stack(c)
d=b.pop()
m=b.push(8)
print(d)
print(m)
from collections import deque
