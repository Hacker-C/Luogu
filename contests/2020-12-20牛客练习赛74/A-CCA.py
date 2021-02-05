n = int(input())
ls = list(map(int, input().split()))
flag1 = flag2 = flag3 = 1
for i in range(0, n - 2):
    if ls[i + 2] - ls[i + 1] != ls[i + 1] - ls[i]:
        flag1 = 0
        break
if 0 not in ls:
    for i in range(0, n - 2):
        if ls[i + 2] / ls[i + 1] != ls[i + 1] / ls[i]:
            flag2 = 0
            break
    for i in range(0, n-2):
        if ls[i + 2] % ls[i + 1] != ls[i + 1] % ls[i]:
            flag3 = 0
            break
else:
    flag2 = flag3 = 0
if flag1 or flag2 or flag3:
    print('YES')
else:
    print('NO')
