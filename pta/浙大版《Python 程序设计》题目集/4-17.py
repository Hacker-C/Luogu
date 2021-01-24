N=int(input())
n=10**(N-1)
m=int('9'*N)
for i in range(n,m+1):
    j=str(i)
    l=len(j)
    sm=0
    for k in range(l):
        sm+=int(j[k])**N
    if sm==i:
        print(i)
