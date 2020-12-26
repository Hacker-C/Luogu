n = int(input())


def isPrime(x):
    if x == 0 or x == 1:
        return 0
    if x == 2 or x == 3:
        return 1
    flag = 1
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            flag = 0

    return flag


for i in range(4, n + 1, 2):
    for j in range(2, i // 2 + 1):
        if isPrime(j) and isPrime(i-j):
            print("{0}={1}+{2}".format(i, j, i-j))
            break

