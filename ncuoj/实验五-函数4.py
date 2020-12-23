import math
n=int(input())
if n<=1:
    print('N')
elif n==2 or n==3:
    print('Y')
else:
    flag=1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            flag=0
            break
    if flag:
        print('Y')
    else:
        print('N')
