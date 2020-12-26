lst = list(map(int, input().split()))
n = len(lst)
ans = 0
for i in lst:
    ans += i * 2 ** (n - 1)
print(ans)
