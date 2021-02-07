n, c = input().split()
n = int(n)
m = n
if n / 2 - n // 2 >= 0.5:
    n = n // 2 + 1
else:
    n = n // 2
for i in range(n):
    if i == 0:
        print(c * m)
    elif i == n - 1:
        print(c * m)
    else:
        print(c + ' ' * (m - 2) + c)
