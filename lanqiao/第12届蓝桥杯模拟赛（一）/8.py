a = 'LANQIAO'
a = 'AAB'
b = 1
while b:
    d = 0
    c = []
    b -= 1
    for i in range(len(a)):
        f = a[:d] + a[d+1:]
        c.append(f)
        print(c)
        d += 1
    a = min(c)
print(a)
    
