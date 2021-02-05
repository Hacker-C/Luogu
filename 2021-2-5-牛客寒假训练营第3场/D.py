n = int(input())
a = sum(list(map(int, list(str(n)))))
m = n + 1
while 1:
    ls = list(map(int, list(str(m))))
    if sum(ls) == a:
        print(m)
        break
    m += 1
