import math as m

x1, y1 = map(float, input().strip('\n\r').split())
x2, y2 = map(float, input().strip('\n\r').split())
x3, y3 = map(float, input().strip('\n\r').split())


def f(a1, b1, a2, b2):
    re = (a1 - a2) * (a1 - a2) + (b1 - b2) * (b1 - b2)
    return m.sqrt(re)


ans = f(x1, y1, x2, y2) + f(x2, y2, x3, y3) + f(x1, y1, x3, y3)

print("{:.2f}".format(ans))
