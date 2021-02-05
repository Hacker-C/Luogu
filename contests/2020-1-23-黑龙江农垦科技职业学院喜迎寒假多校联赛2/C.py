# 前缀和法
n,m=map(int, input().split())
ls=list(map(int, input().split()))
sm=[0 for i in range(n)]
sm[0]=ls[0]
for i in range(1,n):
    sm[i]=sm[i-1]+ls[i]
for i in range(m):
    i,j=map(int, input().split())
    if i==1:
        ans=sm[j-1]
    else:
        ans=sm[j-1]-sm[i-2]
    print(ans)


