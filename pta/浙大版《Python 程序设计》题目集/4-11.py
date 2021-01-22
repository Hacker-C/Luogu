n=int(input())
ans=[]
for i in range(n):
    a=int(input())
    if a==1:
        ans.append('No')
    elif a==2 or a==3:
        ans.append('Yes')
    else:
        flag=1
        for i in range(2, int(a**0.5)+1):
            if a % i==0:
                flag=0
                break
        if flag:
            ans.append('Yes')
        else:
            ans.append('No')
for i in ans:
    print(i)
    

