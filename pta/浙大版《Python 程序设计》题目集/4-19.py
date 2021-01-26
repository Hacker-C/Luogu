n=int(input())
ls=[[] for i in range(n)]
for i in range(n):
    ls1=list(map(int, input().split()))
    ls[i]=ls1
temp=ans=sm=0
for i in range(n):
    sm+=sum(ls[i])
    temp+=ls[i][n-i-1]
    temp+=ls[i][n-1]
    temp+=ls[n-1][i]
temp=temp-(ls[0][n-1]+ls[n-1][0]+ls[n-1][n-1])
print(sm-temp)
