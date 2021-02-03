n=int(input())
t=-1
for i in range(n):
    t=-t
    for j in range(n):
        print(0 if t>0 else 1, end='')
        t=-t
    print()
