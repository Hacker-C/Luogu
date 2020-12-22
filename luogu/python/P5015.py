s = list(input())


def f(x):
    if not (x == ' ' or x == '\n'):
        return x


ans = list(filter(f, s))
print(len(ans))
