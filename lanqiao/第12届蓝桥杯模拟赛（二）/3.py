def f(ls):
    for i in range(len(ls)-1):
        if ls[i]>ls[i+1]:
            return False
    return True
res = 0
_ls = [i for i in range(1, 11)]
for a in _ls:
    for b in _ls:
        for c in _ls:
            for d in _ls:
                for e in _ls:
                    if f([a,b,c,d,e]):
                        res += 1
print(res)
# 2002

