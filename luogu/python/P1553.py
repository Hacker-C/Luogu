def f(ls):
    x = str(int(''.join(ls)))  # 去除开头的0
    reversedX = reversed(x)
    return int(''.join(reversedX))


s = list(input().strip('\n\r'))
if '.' in s:
    i = s.index('.')
    print(str(f(s[:i])) + '.' + str(f(s[i + 1:])))
elif '/' in s:
    i = s.index('/')
    print(str(f(s[:i])) + '/' + str(f(s[i + 1:])))
elif '%' in s:
    print(str(f(s[:-1])) + '%')
else:
    print(f(s))
