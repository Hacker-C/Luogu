n=int(input())
ls = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0 or j == i:
            ls[i][j] = 1
for i in range(2,n):
    for j in range(1,i):
        ls[i][j] = ls[i-1][j-1] + ls[i-1][j]
for i in range(n):
    for j in range(i+1):
        print(ls[i][j], end=' ')
    print()

            
