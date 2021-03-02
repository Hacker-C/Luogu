for i in range(0,32):
    b=bin(i)[2:]
    l=len(b)
    print((5-l)*'0',end='')
    print(b)
