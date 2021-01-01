n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    if x ** 2 + y ** 2 + z ** 2 == 3 * x * y * z:
        print('Yes')
    else:
        print('No')
