n, m = map(int, input().split())
MAX = 0
for i in range(n):
    g = [float(x) for x in input().split()]
    ave = (sum(g) - min(g) - max(g)) / (m-2)
    if ave > MAX:
        MAX = ave
print("{:.2f}".format(MAX))
