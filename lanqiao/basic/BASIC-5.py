n=int(input())
ls=list(map(int, input().split()))
a=int(input())
notFound=True
for i in range(len(ls)):
    if ls[i]==a:
        print(i+1)
        notFound=False
        break
if notFound:
    print(-1)


        
