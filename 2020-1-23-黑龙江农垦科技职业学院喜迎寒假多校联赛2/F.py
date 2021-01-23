n=int(input())
b=bin(n)
b=b.replace('0','1')
ls=list(b)
ls[0]='0'
b=''.join(ls)
print(int(eval(b)))
