n = int(input())
ls = []
for i in range(n):
    ls.append([])
for i in range(len(ls)):
    ls[i] = list(input().split())
test = ''
for i in ls:
    if i[0] == 'a' or i[0] == 'b' or i[0] == 'c':
        test = i[0]
    if len(i) == 3:
        x = i[1]
        y = i[2]
    else:
        x = i[0]
        y = i[1]
    if test == 'a':
        print("{0}+{1}={2}".format(x, y, int(x) + int(y)))
        print(len(x) + len(y) + 2 + len(str(int(x) + int(y))))
    if test == 'b':
        print("{0}-{1}={2}".format(x, y, int(x) - int(y)))
        print(len(x) + len(y) + 2 + len(str(int(x) - int(y))))
    if test == 'c':
        print("{0}*{1}={2}".format(x, y, int(x) * int(y)))
        print(len(x) + len(y) + 2 + len(str(int(x) * int(y))))