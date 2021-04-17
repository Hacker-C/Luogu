def f(n):
    a=1
    b=0
    for _ in range(n):
        a,b=b,a+b
    return a
def g(n):
    if n==1 or n==2:
        return n-1
    return g(n-1)+g(n-2)
import math as m
def w(n):
    for i in range(2, int(m.sqrt(n))+1):
        if  n%i==0:
            return False
    return True
print(w(33))
