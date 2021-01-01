a, b = map(int, input().split())


def f(x):
    re = 1
    for i in range(1, x + 1):
        re *= i
    return re


flag = 1
for i in range(a, b + 1):
    if f(i)%(i ** 2 + 1) == 0:
        print(i)
        flag = 0
if flag:
    print('None')
