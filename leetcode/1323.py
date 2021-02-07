ls=list(input())
if '6' not in ls:
    print(int(''.join(ls)))
else:
    for i in range(len(ls)):
        if ls[i] == '6':
            ls[i] = '9'
            break
    
    print(int(''.join(ls)))
