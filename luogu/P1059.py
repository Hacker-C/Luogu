n=int(input())
ls=list(map(int,input().split()))
ls=list(set(ls))
l=len(ls)
print(l)
for i in sorted(ls):
    print(i, end=' ')
