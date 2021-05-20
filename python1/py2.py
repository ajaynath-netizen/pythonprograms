def ols(func):
    
    def wrap(*args):
            print('writin recursion')
            x=func(*args)
            return x
    return wrap

            
@ols
def drift(i):

    if i<=0:
        return 1
    else:
        return i*drift(i-1)
i=8
print(drift(i))



def dls(num1):
    def rls(func):
        def mls(*arg):
           print("before ")
           x=func(num1+arg[0])
           print("after")
           return x
        return mls

    return rls

@dls(10)
def fun(n):
    return n*n

print(fun(5))
# print(dls(5)(fun)(6))