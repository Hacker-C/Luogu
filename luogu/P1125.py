word = input()
dct = dict()
for s in word:
    if s not in dct.keys():
        dct[s] = 1
    else:
        dct[s] += 1
t = sorted(dct.items(), key=lambda x: x[1], reverse=True)
num = t[0][1] - t[-1][1]


def f(x):
    if x == 0 or x == 1:
        return 0
    if x == 2:
        return 1
    flag = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            flag = 0
    return flag


if f(num):
    print('Lucky Word')
    print(num)
else:
    print('No Answer')
    print(0)
