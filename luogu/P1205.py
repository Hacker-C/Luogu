n = int(input())
ls = []
compare = []
for i in range(n):
    ls.append(list(input()))

for i in range(n):
    compare.append(list(input()))


def f1(lst1, comp, m):
    lst2 = [[j for j in range(m)] for i in range(m)]
    for k in range(m):
        for j in range(n - 1, -1, -1):
            lst2[k][n - j - 1] = lst1[j][k]
    if lst2 == comp:
        return 1
    return 0


def f2(lst1, comp, m):
    lst2 = [[j for j in range(m)] for i in range(m)]
    for j in range(m - 1, -1, -1):
        for k in range(m - 1, -1, -1):
            lst2[j][k] = lst1[m - 1 - j][m - 1 - k]
    if lst2 == comp:
        return 1
    return 0


def f3(lst1, comp, m):
    lst2 = [[j for j in range(m)] for i in range(m)]
    for j in range(m):
        for k in range(m - 1, -1, -1):
            lst2[k][j] = lst1[j][m - 1 - k]
    if lst2 == comp:
        return 1
    return 0


def f4(lst1, comp, m):
    lst2 = [[j for j in range(m)] for i in range(m)]
    for j in range(m):
        for k in range(m):
            lst2[j][m - k - 1] = lst1[j][k]
    return lst2


def f5(lst1, comp, m):
    temp = f4(lst1, comp, m)
    if f1(temp, comp, m):
        return 1
    if f2(temp, comp, m):
        return 1
    if f3(temp, comp, m):
        return 1
    return 0


if f1(ls, compare, n):
    print(1)
    exit(0)
if f2(ls, compare, n):
    print(2)
    exit(0)
if f3(ls, compare, n):
    print(3)
    exit(0)
if f4(ls, compare, n) == compare:
    print(4)
    exit(0)
if f5(ls, compare, n):
    print(5)
    exit(0)
if ls == compare:
    print(6)
    exit(0)
print(7)
exit(0)

