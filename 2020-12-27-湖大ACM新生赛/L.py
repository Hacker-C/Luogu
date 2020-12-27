# 未过
n = int(input())


def f(a1, b1, a2, b2):
    return (a1 - a2) ** 2 + (b1 - b2) ** 2


for i in range(n):
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    x3, y3 = map(float, input().split())
    x4, y4 = map(float, input().split())
    a_2 = f(x1, y1, x2, y2)
    b1_2 = f(x1, y1, x3, y3)
    c1_2 = f(x2, y2, x3, y3)
    b2_2 = f(x1, y1, x4, y4)
    c2_2 = f(x2, y2, x4, y4)
    if (b1_2 + c1_2 - a_2) ** 2 * b2_2 * c2_2 == (b2_2 + c2_2 - a_2) ** 2 * b1_2 * c1_2:
        print('yes')
    else:
        print('no')
