n = int(input())
dct = dict()
for i in range(n):
    x, y = map(int, input().split())
    dct[i + 1] = [x * y, x]
d_order = sorted(dct.items(), key=lambda k: (k[1][0], k[1][1]), reverse=True)
for e in d_order:
    print(e[0], end=' ')
