s = set()
for i in range(1, 2021):
    if 2020 % i==0:
        s.add(i)
print(len(s)) # 12
