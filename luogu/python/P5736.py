n = int(input())
ls = list(map(int, input().split()))


def f(x):
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    flag = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = False
    return flag


for i in ls:
    if f(i):
        print(i, end=' ')
