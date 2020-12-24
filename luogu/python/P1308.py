word = input().strip('\n\r').lower()
l = input().strip('\n\r').lower()
x = ' ' + word + ' '
ans1 = 0
i1 = i2 = i3 = 1000010
length = len(word)
if l[:length+1] == word + ' ':
    ans1 += 1
    i1 = 0
if l[len(l) - length+1:] == ' ' + word:
    ans1 += 1
    i2 = len(l) - length
for i in range(len(l)):
    if l[i:i+length] == word and l[i-1] == ' ' and l[i+length] == ' ':
        ans1 += 1
if x in l:
    i3 = l.index(x) + 1
if ans1 == 0:
    print(-1)
else:
    print(ans1, min(i1, i2, i3))

