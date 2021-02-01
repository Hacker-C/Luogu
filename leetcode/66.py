digits = [1,2,3,9]
digits = [4,3,2,1]
digits=[0,0,0,0]
l=len(digits)
digits=list(map(str, digits))
num=int(''.join(digits))
if num==0:
    ans=[0 for i in range(l)]
    ans[-1]=1
    print(ans)
else:
    num+=1
    ans=list(str(num))
    ans=list(map(int, ans))
    print(ans)
