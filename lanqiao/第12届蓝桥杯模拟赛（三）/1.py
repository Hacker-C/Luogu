def f(a, b):
    m = min(a,b)
    for i in range(m, -1, -1):
        if a%i==0 and b%i==0:
            return i==1
ans = 0
for i in range(1, 2021):
    if f(i, 2020):
        ans += 1
print(ans)
