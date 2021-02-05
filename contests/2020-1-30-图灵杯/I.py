ls=[1,2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
sm=[3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767]
t=int(input())
for i in range(t):
    n=int(input())
    flag=1
    for j in sm:
        if n%j==0:
            print('YE5')
            flag=0
            break
    if flag:
        print('N0')
