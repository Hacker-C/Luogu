n=int(input())
if n==1:
    print(0, 0)
    exit(0)
ls=[[] for i in range(n)]
for i in range(n):
    ls1=list(map(int,input().split()))
    ls[i]=ls1
flag=0
for i in range(n):
    mx=max(ls[i])
    eLst=[]
    for e in range(n):
        if ls[i][e]==mx:
            eLst.append(e)
    for indexJ in eLst: 
        minJ=ls[0][indexJ]
        for j in range(n):
            if ls[j][indexJ]<minJ:
                minJ=ls[j][indexJ]
        if mx==minJ:
            flag=1
            ansI=i
            ansJ=indexJ
            break
    if flag:
        break
        
if flag:
    print(ansI, ansJ)
else:
    print('NONE')
