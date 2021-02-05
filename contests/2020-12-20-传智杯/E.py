n, k = map(int, input().split())
s = 0
ls = []
MIN = int('1'*n)
MAX = int('6'*n)
for i in range(MIN, MAX + 1):
    if i % k == 0:
        s += 1
print(s % (10 ** 9 + 7))
