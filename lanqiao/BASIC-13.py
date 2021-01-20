def bubbleSort(ls):
    l=len(ls)
    for i in range(l):
        for j in range(l-i-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls
n = int(input())
ls = list(map(int, input().split()))
ans = bubbleSort(ls)
for i in ans:
    print(i, end=' ')
