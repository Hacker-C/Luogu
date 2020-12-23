a,b,c=map(float, input().split())
deta=b*b-4*a*c
if deta==0:
    print("{:.3f}".format(-b*(2*a)))
elif deta<0:
    print('No root')
else:
    x1=(-b+deta**0.5)/(2*a)
    x2=(-b-deta**0.5)/(2*a)
    print("{0:.2f} {1:.2f}".format(x1,x2))
