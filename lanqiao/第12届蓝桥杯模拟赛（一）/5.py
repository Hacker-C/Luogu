a = [87, 39, 35, 1, 99, 10, 54, 1, 46, 24, 74, 62, 49, 13, 2, 80, 24, 58, 8, 14, 83, 23, 97, 85, 3, 2, 86, 10, 71, 15]
ans = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            ans += 1
print(ans)
# 217
