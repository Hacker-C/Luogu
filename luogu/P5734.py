n = int(input().strip('\r\n'))
s = list(input().strip('\r\n'))
for i in range(n):
    cmd = list(input().split())
    if cmd[0] == '1':
        for j in cmd[1]:
            s.append(j)
        print(''.join(s))
    if cmd[0] == '2':
        s = s[int(cmd[1]): int(cmd[1]) + int(cmd[2])]
        print(''.join(s))
    if cmd[0] == '3':
        s = list(''.join(s)[:int(cmd[1])] + cmd[2] + ''.join(s)[int(cmd[1]):])
        print(''.join(s))
    if cmd[0] == '4':
        if cmd[1] in ''.join(s):
            print(''.join(s).index(cmd[1]))
        else:
            print(-1)
