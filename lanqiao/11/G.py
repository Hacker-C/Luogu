s=input()
dct=dict()
for i in s:
    if i in dct.keys():
        dct[i] += 1
    else:
        dct[i] = 1
ls = sorted(dct.items())
print(ls[0][0])
print(ls[0][1])

