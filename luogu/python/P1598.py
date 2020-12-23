ls = []
for i in range(4):
    x = list(input().strip('\n\r'))
    for j in x:
        if 65 <= ord(j) <= 90:
            ls.append(j)
dct = {}
for i in range(65, 91):
    dct[chr(i)] = ls.count(chr(i))
x = max(dct.values())
# 26行 x列
temp = [[' ' for i in range(x + 1)] for j in range(26)]
for i in range(26):
    l = chr(65 + i)
    temp[i][0] = l
    for j in range(1, dct[l] + 1):
        temp[i][j] = '*'

m = 26
n = x + 1

# for i in temp:
#     for j in i:
#         print(j, end='')
#     print()

ans = [[' ' for i in range(m)] for j in range(n)]
for i in range(m):
    for j in range(n):
        ans[n-j-1][i] = temp[i][j]
for i in ans:
    for j in i[:-1]:
        print(j, end=' ')
    print(i[-1], end='')
    print()
