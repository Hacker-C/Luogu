n = int(input())


def f(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * f(x - 1)


print(f(n))
