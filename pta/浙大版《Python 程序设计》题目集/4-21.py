T=int(input())
for i in range(T):
    n=int(input())
    ls=[[] for i in range(n)]
    for i in range(n):
        ls1=list(map(int, input().split()))
        ls[i]=ls1
    flag=0
    for i in range(1,n):
        for j in range(0, i):
            if ls[i][j]!=0:
                flag=1
                break
        if flag:
            break
    if flag:
        print('NO')
    else:
        print('YES')

    
