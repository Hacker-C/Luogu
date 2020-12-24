x, y = [int(x) for x in input().split()]


def f(n):
    if (n % 4 == 0 and n % 400 != 0) or n % 200 == 0:
        return True
    else:
        return False


s = 0
for i in range(x, y + 1):
    if f(i):
        s += 1
print(s)
for i in range(x, y + 1):
    if f(i):
        print(i, end=' ')
