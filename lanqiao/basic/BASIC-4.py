n=int(input())
ls=list(map(int, input().split()))
mi=ls[0]
ma=ls[0]
su=0
for i in range(n):
    if ls[i]<mi:
        mi=ls[i]
    if ls[i]>ma:
        ma=ls[i]
    su+=ls[i]
print(ma)
print(mi)
print(su)
