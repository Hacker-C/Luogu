import math

M, N = map(int, input().split())
print(math.gcd(M, N), end=' ')
print(int(M * N / math.gcd(M, N)))
