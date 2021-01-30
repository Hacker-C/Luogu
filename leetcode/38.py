n=int(input())
ans='1'
k=0
temp=ans[0]
for i in range(n):
    for i in range(0,len(ans)):
        if ans[i]==temp:
            k+=1
        else:
            ans+=temp*k
            k=0
            temp=ans[i]
print(ans)
