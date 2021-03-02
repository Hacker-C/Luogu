n = int(input())
n1, n2 = 0, 0
for i in range(n):
    a = int(input())
    if a >= 60:
        n1 += 1
    if a >= 85:
        n2 += 1
ans1 = int(n1 / n * 100)
ans2 = int(n2 / n * 100)
if n1 / n * 100 - ans1 >= 0.5:
    ans1 += 1
if n2 / n * 100 -ans2 >= 0.5:
    ans2 += 1
print("{0}%".format(ans1))
print("{0}%".format(ans2))
