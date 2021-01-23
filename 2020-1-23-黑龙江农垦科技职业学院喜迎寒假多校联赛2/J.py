n=int(input())
ls=list(map(int, input().split()))
mi=min(ls)
for i in range(len(ls)):
    if ls[i]==mi:
        print(i+1)
        break
