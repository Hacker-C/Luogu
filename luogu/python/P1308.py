# 未完成...
word = input().strip('\n\r').lower()
ss = input().strip('\n\r').lower()

sss = list(ss)
lst = ss.split()

l = len(word)

if word in lst:
    print(lst.count(word), end=' ')
    if ''.join(sss[0:l]) == word and ss[l] == ' ':
        print(0)
    else:
        for i in range(1, len(sss)-l):
            if ''.join(sss[i:i+l]) == word and sss[i-1] == ' ' and sss[i+l+1] == ' ':
                print(i)
                exit(0)
        if ''.join(sss[l-1:]) == word:
            print(len(sss)-l+1)
            exit(0)
else:
    print(-1)
