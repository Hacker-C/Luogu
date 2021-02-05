n = int(input())
for i in range(n):
    a, b = input().split()
    if a == '2' and b == '4':
        print('{0} sheng {1}'.format(a, b))
    elif a == '4' and b == '2':
        print('{0} sheng {1}'.format(b, a))

    elif a == '4' and b == '5':
        print('{0} sheng {1}'.format(a, b))
    elif a == '5' and b == '4':
        print('{} sheng {}'.format(b, a))

    elif a == '5' and b == '1':
        print('{} sheng {}'.format(a, b))
    elif a == '1' and b == '5':
        print('{} sheng {}'.format(b, a))

    elif a == '1' and b == '3':
        print('{} sheng {}'.format(a, b))
    elif a == '3' and b == '1':
        print('{} sheng {}'.format(b, a))

    elif a == '3' and b == '2':
        print('{} sheng {}'.format(a, b))
    elif a == '2' and b == '3':
        print('{} sheng {}'.format(b, a))

    elif a == '1' and b == '2':
        print('{} ke {}'.format(a, b))
    elif a == '2' and b == '1':
        print('{} ke {}'.format(b, a))

    elif a == '2' and b == '5':
        print('{} ke {}'.format(a, b))
    elif a == '5' and b == '2':
        print('{} ke {}'.format(b, a))

    elif a == '5' and b == '3':
        print('{} ke {}'.format(a, b))
    elif a == '3' and b == '5':
        print('{} ke {}'.format(b, a))

    elif a == '3' and b == '4':
        print('{} ke {}'.format(a, b))
    elif a == '4' and b == '3':
        print('{} ke {}'.format(b, a))

    elif a == '4' and b == '1':
        print('{} ke {}'.format(a, b))
    elif a == '1' and b == '4':
        print('{} ke {}'.format(b, a))
