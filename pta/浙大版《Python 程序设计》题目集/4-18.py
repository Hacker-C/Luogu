N=int(input())
ls=[i+1 for i in range(N)]
if N==1:
    print(1)
else:
    while len(ls)>=3:
        del ls[2]
        ls.append(ls.pop(0))
        ls.append(ls.pop(0))
    print(ls[1])
