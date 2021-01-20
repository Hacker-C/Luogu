dct={
    '0':1,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}
ans=[]
n = int(input())
for i in range(n):
    hx=input()
    temp=0
    l = len(hx)
    for i in range(l):
        temp += dct[hx[l-i-1]]*16**i
    ls = []
    while temp>0:
        ls.append(temp % 8)
        temp //= 8
    ls2=[]
    for i in range(len(ls)-1,-1,-1):
        ls2.append(str(ls[i]))
    ans.append(''.join(ls2))
for i in ans:
    print(i)

