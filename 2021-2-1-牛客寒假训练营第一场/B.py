k = int(input())
if k == 0:
    print('')
else:
    ans=[]
    k0 = int(k ** 0.5)
    k1 = k - k0 ** 2
    n = k0 + k1
    # print('(', end='')
    ans.append('(')
    for i in range(k1):
        # print(')', end='')
        ans.append(')')
    for i in range(k0 - 1):
        # print('(', end='')
        ans.append('(')
    for i in range(k0):
        # print(')', end='')
        ans.append(')')
    print(ans)
