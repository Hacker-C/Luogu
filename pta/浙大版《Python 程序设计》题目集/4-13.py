error=float(input())
i=1
j=0
e=0
while 1:
    if j>0:
        i=i*j
    e+=1/i
    j+=1
    if 1/(i*j)<error:
        print("{:.6f}".format(e+1/(i*j)))
        break
    

