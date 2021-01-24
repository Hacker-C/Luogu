a,b,c=map(int,input().split())
def s(x,y,z):
    if x+y>z:
        return 1
    else:
        return 0
if s(a,b,c) and s(a,c,b) and s(b,c,a):
    print('yes')
else:
    print('no')
