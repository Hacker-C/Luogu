ls = []
for i in range(int(input().strip('\n\r'))):
    ls.append(input().strip('\n\r').split())
for elem in sorted(ls, reverse=True):
    print(elem[0], elem[1])
for i in range(len(ls)):
    ls[i][0], ls[i][1] = ls[i][1], ls[i][0]
    ls[i][0] = int(ls[i][0])
print()


def f(x):
    def g(y):
        return chr(187 - ord(y))
    return ''.join(list(map(g, x)))


for elem in sorted(ls, key=lambda x: (x[0], f(x[1])), reverse=True):
    print(elem[1], elem[0])
