def f(a,b):
    _min = min(a,b)
    for i in range(_min,0,-1):
        if a%i==0 and b%i==0:
            return i
def g(a,b):
    while a!=b:
        c=a%b
        a=b
        b=c
    return a
print(g(16,24))
