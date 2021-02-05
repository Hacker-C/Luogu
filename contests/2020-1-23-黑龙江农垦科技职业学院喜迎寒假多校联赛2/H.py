n=int(input())
ls=[]
for i in range(n):
    ls1=input().split()
    ls.append(ls1)
ls=sorted(ls,key=lambda x:x[0])
l=len(ls)
for i in range(l):
    for j in range(l-i-1):
        if (len(ls[j][0])>len(ls[j+1][0])):
            ls[j],ls[j+1]=ls[j+1],ls[j]
for i in ls:
    for j in i:
        print(j,end=' ')
    print()
