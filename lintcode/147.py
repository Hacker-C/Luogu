def getNarcissisticNumbers(n):
    # write your code here
    if n == 1:
        print(0)
    l=10**(n-1)
    m=int('9'*n)
    for i in range(l,m+1):
        j=str(i)
        l=len(j)
        sm=0
        for k in range(l):
            sm+=int(j[k])**n
        if sm==i:
            print(i)
getNarcissisticNumbers(1)
