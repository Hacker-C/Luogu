x = input().strip('\n\r')
y = input().strip('\n\r')
sx = sy = 1
for i in x:
    sx *= ord(i) - 64
for i in y:
    sy *= ord(i) - 64
if sx % 47 == sy % 47:
    print('GO')
else:
    print('STAY')
