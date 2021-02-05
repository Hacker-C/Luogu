n=int(input())
ans=0
for k in range(2,n+1):
    num=k
    m=[]
    while k!=1:
        for i in range(2,k+1):
            if k % i == 0:
                m.append(str(i))
                k = k//i
                break
    ans+=int(''.join(m))
    ans%=1e9+7
print(int(ans))
