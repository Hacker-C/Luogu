nums = [16, 36, 49, 64]


def f(x):
    print('运行了函数f(x)1次。')
    return x ** 0.5


print([n for i in nums if (n := f(i)) > 5])

print([f(i) for i in nums if f(i) > 5])
