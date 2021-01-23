x=input()
flag=0
if x[0]=='-':
    x=x[1:]
    flag=1
x=''.join(list(reversed(x)))
x=int(x)
x=str(x)
if flag:
    x='-'+x
print(x)
    
