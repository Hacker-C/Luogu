s = input().strip('\n\r')
x = y = 0
x += s.count('boy')
y += s.count('girl')
s = s.replace('boy', '...')
s = s.replace('girl', '....')

x += s.count('b')
x += s.count('o')
x += s.count('y')

x -= s.count('bo')
x -= s.count('oy')

y += s.count('g')
y += s.count('i')
y += s.count('r')
y += s.count('l')

y -= s.count('gir') * 2
y -= s.count('irl') * 2

s = s.replace('gir', '...')
s = s.replace('irl', '....')

y -= s.count('gi')
y -= s.count('ir')
y -= s.count('rl')

print(x)
print(y)
