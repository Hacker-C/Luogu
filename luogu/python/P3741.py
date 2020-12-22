n = int(input())
ls = list(input().strip('\n\r'))
m = ''.join(ls).count('VK')
for i in range(n):
    new1 = list(ls)
    new1[i] = 'K'
    new2 = ''.join(new1)
    if new2.count('VK') > m:
        m = new2.count('VK')
    new1 = list(ls)
    new1[i] = 'V'
    new2 = ''.join(new1)
    if new2.count('VK') > m:
        m = new2.count('VK')
print(m)
        
