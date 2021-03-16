n = int(input())
ls = list(map(int, input().split()))
max = 0
for i in range(n-1):
    if ls[i+1] - ls[i] > max:
        max = ls[i+1] - ls[i]
print(max)
