n = int(input())
for i in range(n):
    m = int(input())
    a = 0
    b = 1
    for i in range(m):
        a, b = b, a + b
    print(a, b)