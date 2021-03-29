def f(x):
    if x==1:
        return 1
    return x * f(x-1)
n = 1
while n * (n-1)/2 <2020:
    n += 1
print(n)
# 65
