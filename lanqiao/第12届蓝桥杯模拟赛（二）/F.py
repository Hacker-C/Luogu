a = int(input())
b = int(input())
t = int(input())
h = t // 60
m = t % 60
b += m
h1 = b // 60
m1 = b % 60
b %= 60
print(a+h+h1)
print(b)
