def f(x):
    ls = reversed(list(str(x)))
    return ''.join(ls)
for i in range(1000, 10000):
    if str(i) == f(i):
        print(i)

