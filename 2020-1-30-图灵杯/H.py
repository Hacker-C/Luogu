def A(n,m):
    if n==1 and m==0:
        return 2
    if n==0 and m>=0:
        return 1
    if n>=2 and m==0:
        return n+2
    if m==0:
        return n
    if m==1:
        return 2*n
    if m==2:
        return 2**n
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(A(n,m)%998244353)
