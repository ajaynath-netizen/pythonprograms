import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr.shape)

# arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.size)
# for dimensions
print(arr.ndim)
# to append ,we can't append directly to array
print(np.append(arr[0],88))
print(arr)
# arrays are immutable
arr=np.array([[5,63,8],[5,6,43],[1,6,4]])
print(arr.shape)
print(arr[1,2])
print(arr)
a='ajay is freat\ndonkey '
a=a.rstrip('\n')

a=a.encode()
c="5".encode()
b=chr(97)
b=ord(b)
print(ord('9'))
# print(a.rstrip('nokdey'))
print(a,b,c)
a=" ".join(["the natural numbers from {}-{} :".format(1,3),str(["{} ".format(i) for i in range(3)])])

print(a)

# c=[]
# for i in range(6):
#     c[i]=[]
#     for j in range(3):
#      c[i].append(j)
    
#      print(c)

print(c)
c=[7,963,45,3,3,158,3,43,7,2]
# for i in range(len(c)):
#     for j in range(len(c)-i):
        
#         if c[i]>c[j+1]:
#             large=c[i]
#         else:

#             large=c[j+1]
a=[i for i in range(5)]
b=[m*m for m in range(5)]
print(b)
c={k:v for k,v in map(list,zip(a,b))}
d=list(map(list,zip(a,b)))
print(d)
print(c)
e=[(k,v) for k in range(6) for v in range(6)]
print(e)